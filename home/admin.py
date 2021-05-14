from django.contrib import admin
from .models import SiteReviews


class SiteReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'date',
        'review',
        'rating',
    )


admin.site.register(SiteReviews, SiteReviewsAdmin)
