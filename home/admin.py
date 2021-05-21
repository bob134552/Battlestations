from django.contrib import admin
from .models import SiteReviews


class SiteReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'date',
        'review',
        'rating',
    )

    readonly_fields = ('date',)

    fields = (
        'date',
        'user',
        'review',
        'rating',)

    ordering = ('-date',)


admin.site.register(SiteReviews, SiteReviewsAdmin)
