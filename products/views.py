from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from random import randrange

from .models import Product, Category, Comment
from .forms import ProductForm, CommentForm


def all_products(request):
    """A view to display all products"""
    products = Product.objects.exclude(category__name='custom_build')
    query = None
    categories = None
    sort = None
    direction = None
    template = 'products/products.html'

    # Allows sorting based on category.
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            if request.GET['category'] == 'pre_built':
                products = products.filter(category__name='pre_built')
                template = 'products/search.html'

        # Allows searching based on user input to the searchbar
        if 'q' in request.GET:
            template = 'products/search.html'
            query = request.GET['q']

            if not query:
                messages.error(request,
                               'You haven\'t entered anything to search for.')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                info__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, template, context)


def product_details(request, product_id):
    """A view to display product details and comments"""
    product = get_object_or_404(Product, pk=product_id)
    comments = product.comments.filter(product=product)
    new_comment = None

    if request.method == 'POST':
        form_data = {
            'username': request.user if request.user else 'AnonymousUser',
            'body': request.POST['body'],
        }
        comment_form = CommentForm(form_data)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            messages.success(request, 'Comment submitted. Thank you!')
            new_comment.save()
            return redirect(reverse('product_details', args=[product.id]))
    comment_form = CommentForm()
    context = {
        'product': product,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def update_comment(request, comment_id):
    '''
    Allows users to edit comments they have left on products,
    data is sent through a ajax POST.
    '''
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        try:
            form_data = {
                'username': request.user if request.user else 'AnonymousUser',
                'body': request.POST['body'],
            }
            comment_form = CommentForm(form_data, instance=comment)
            if comment_form.is_valid():
                comment_form.save()
                return HttpResponse(content='Comment updated!', status=200)
            else:
                return HttpResponse(content='Unable to update comment',
                                    status=200)
        except Exception as e:
            return HttpResponse(
                    content=f'ERROR: {e}',
                    status=500)


@login_required
def delete_comment(request, product_id, comment_id):
    '''Lets users delete their comments'''
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.username or request.user.is_superuser:
        comment.delete()
        return redirect(reverse('product_details', args=[product_id]))
    else:
        messages.error(request, 'Sorry can only delete your own comments.')
        return redirect(reverse('product_details', args=[product_id]))


@login_required
def add_product(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return(redirect(reverse('home')))
    else:
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save()
                messages.success(request, 'Successfully added product.')
                return redirect(reverse('product_details', args=[product.id]))
            else:
                messages.error(request, 'Failed to add product. \
                    Please check that the form is valid.')
        else:
            form = ProductForm()
        template = 'products/add_product.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


@login_required
def update_product(request, product_id):
    """Update a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return(redirect(reverse('home')))
    else:
        product = get_object_or_404(Product, pk=product_id)
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request,
                                 f'Update for {product.name} successful.')
                return redirect(reverse('product_details', args=[product.id]))
            else:
                messages.error(request, 'Error updating, \
                    please ensure form is valid.')
        else:
            form = ProductForm(instance=product)
            messages.info(request, f'Editing {product.name}')

        template = 'products/update_product.html'
        context = {
            'form': form,
            'product': product,
        }

        return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Removes product from store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return(redirect(reverse('home')))
    else:
        product = get_object_or_404(Product, pk=product_id)
        messages.success(request, f'{product.name} deleted from store.')
        product.delete()
        return redirect(reverse('products'))


def custom_build(request):
    '''
    Renders the custom build page and fills
    each form select input with relevant product
    data.
    '''
    products = Product.objects.exclude(
        category__name=('pre_built', 'custom_build'))
    template = 'products/custom_build.html'
    context = {
        'products': products,
    }

    return render(request, template, context)


def add_custom_to_basket(request):
    '''Creates and adds custom built pc to product model and basket'''
    basket = request.session.get('basket', {})
    x = str(randrange(0, 999999)).zfill(6)
    custom_pc_data = request.POST
    custom_pc_form = ProductForm({
        'sku': f'CB{x}',
        'category': 11,
        'name': custom_pc_data['name'],
        'image': custom_pc_data['image'],
        'description': custom_pc_data['description'],
        'price': custom_pc_data['total'],
    })

    if custom_pc_form.is_valid():
        custom_pc = Product(
            category=Category.objects.get(pk=11),
            sku=f'CB{x}',
            name=custom_pc_data['name'],
            image=custom_pc_data['image'].split('/media/')[1],
            description=custom_pc_data['description'],
            price=custom_pc_data['total'],
        )
        custom_pc.save(force_insert=True)
        quantity = int(request.POST.get('quantity'))
        basket[custom_pc.id] = quantity
        request.session['basket'] = basket
        messages.success(request, 'Successfully added custom build to basket.')
        return HttpResponse(
                content='Added Custom Build To Basket',
                status=200)
    else:
        return HttpResponse(
            content='Unable to add build.',
            status=200
        )
