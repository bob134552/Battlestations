from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>', views.product_details, name='product_details'),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:product_id>', views.update_product, name='update_product'),
    path('delete/<int:product_id>', views.delete_product, name='delete_product'),
    path('delete_comment/<int:product_id>/<int:comment_id>', views.delete_comment, name='delete_comment'),
    path('update_comment/<int:comment_id>', views.update_comment, name='update_comment'),
    path('custom_build/', views.custom_build, name='custom_build'),
]
