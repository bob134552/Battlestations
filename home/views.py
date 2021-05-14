from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product
from .forms import SiteReviewsForm
from .models import SiteReviews
from django.contrib.auth.models import User


def index(request):
    '''A view to return the index page'''
    if request.method == 'POST':
        user = get_object_or_404(User, username=request.user)
        form_data = {
            'user': user.id,
            'rating': request.POST['rating'],
            'review': request.POST['review'],
        }

        review_form = SiteReviewsForm(form_data)
        if review_form.is_valid():
            review_form.save()
            messages.success(request, 'Review submitted. Thank you!')
        else:
            messages.error(request, 'Have you already submitted a review? \
                If not, please check that the form is valid.')

    products = Product.objects.filter(category__name='pre_built')[:3]
    reviews = SiteReviews.objects.all()[:4]
    review_form = SiteReviewsForm()
    context = {
        'products': products,
        'reviews': reviews,
        'review_form': review_form,
    }
    return render(request, 'home/index.html', context)
