from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_basket, name='show_basket'),
    path('add/<product_id>/', views.add_to_basket, name='add_to_basket'),
    path('adjust/<product_id>/', views.adjust_basket, name='adjust_basket'),
    path('remove/<product_id>/',
         views.remove_from_basket, name='remove_from_basket'),
]
