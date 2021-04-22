from django.shortcuts import render, redirect


def show_basket(request):
    '''Renders the basket page'''

    return render(request, 'basket/basket.html')


def add_to_basket(request, product_id):
    '''Adds products to basket'''

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if product_id in list(basket.keys()):
        basket[product_id] += quantity
    else:
        basket[product_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)
