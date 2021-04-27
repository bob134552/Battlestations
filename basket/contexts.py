from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal


def basket_items(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for product_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=product_id)
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    final_amount = total + delivery

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'final_amount': final_amount,
    }

    return context
