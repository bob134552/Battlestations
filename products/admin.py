from django.contrib import admin
from .models import Product, Category, Comment


class ProductCommentAdmin(admin.StackedInline):
    model = Comment
    list_display = (
        'username',
        'body',
        'product',
        'created',
    )


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductCommentAdmin,)
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
        'in_stock',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
