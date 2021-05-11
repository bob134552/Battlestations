from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """A view to display all products"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    template = 'products/products.html'

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
    """A view to display product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)


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
