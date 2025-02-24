from django.urls import path
from crud import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create_user),
    path('edit/', views.edit_user, name='edit_user'),
    path('edit/<int:user_id>', views.edit_user_page),
]