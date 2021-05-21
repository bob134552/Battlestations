from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_review/', views.add_review, name='add_review'),
    path('update_review/<int:review_id>',
         views.update_review, name='update_review'),
    path('delete_review/<int:review_id>',
         views.delete_review, name='delete_review'),
]
