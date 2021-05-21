from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .forms import SiteReviewsForm
from .models import SiteReviews
from django.contrib.auth.models import User
from django.db.models import Avg


def index(request):
    '''
    A view to return the index page and display
    site reviews and average site rating.
    '''
    products = Product.objects.filter(category__name='pre_built')[:3]
    reviews = SiteReviews.objects.all()[:4]
    overall = SiteReviews.objects.aggregate(Avg('rating'))
    rating_avg = None
    if overall['rating__avg'] is not None:
        rating_avg = round(overall['rating__avg'])

    context = {
        'rating_avg': rating_avg,
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'home/index.html', context)


@login_required
def add_review(request):
    '''Allows a logged in user to leave a review'''
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
            return redirect('home')
        else:
            messages.error(request, 'Have you already submitted a review? \
                If not, please check that the form is valid.')

    review_form = SiteReviewsForm()

    context = {
        'review_form': review_form,
    }
    template = 'home/add_review.html'

    return render(request, template, context)


@login_required
def update_review(request, review_id):
    '''Updates user review'''
    review = get_object_or_404(SiteReviews, pk=review_id)
    if request.method == 'POST':
        review_form = SiteReviewsForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            messages.success(request, 'Review updated. Thank you!')
            return redirect('home')
        else:
            messages.error(request, 'Please check that the form is valid.')

    review_form = SiteReviewsForm(instance=review)

    context = {
        'review_form': review_form,
        'review': review,
    }
    template = 'home/update_review.html'

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    '''Deletes user review.'''
    review = get_object_or_404(SiteReviews, pk=review_id)
    if request.user == review.user or request.user.is_superuser:
        review.delete()
        return redirect(reverse('home'))
    else:
        messages.error(request, 'Sorry can only delete your own review.')
        return (redirect(reverse('home')))
