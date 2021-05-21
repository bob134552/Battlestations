from django.shortcuts import (render, redirect,
                              reverse, HttpResponse,
                              get_object_or_404)
from products.models import Product
from django.contrib import messages


def show_basket(request):
    '''Renders the basket page'''

    return render(request, 'basket/basket.html')


def add_to_basket(request, product_id):
    '''Adds products to basket'''

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if product_id in list(basket.keys()):
        basket[product_id] += quantity
        messages.success(request,
                         f'Updated {product.name} quantity \
                        to {basket[product_id]}.')
    else:
        basket[product_id] = quantity
        messages.success(request, f'Added {product.name} to your basket!')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, product_id):
    '''Adds product quantity in the basket'''
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[product_id] = quantity
        messages.success(request,
                         f'Updated {product.name} quantity to \
                        {basket[product_id]}')
    else:
        basket.pop(product_id)
        messages.success(request, f'Removed {product.name} from your basket.')

    request.session['basket'] = basket
    return redirect(reverse('show_basket'))


def remove_from_basket(request, product_id):
    '''Remove product from basket'''
    try:
        product = get_object_or_404(Product, pk=product_id)
        basket = request.session.get('basket', {})
        # Deletes custom built pc on removal from basket
        if product.category.name == 'custom_build':
            product.delete()
        basket.pop(product_id)
        messages.success(request, f'Removed {product.name} from your basket.')
        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
