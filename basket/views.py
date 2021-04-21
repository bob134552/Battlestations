from django.shortcuts import render


def show_basket(request):
    '''Renders the basket page'''

    return render(request, 'basket/basket.html')
