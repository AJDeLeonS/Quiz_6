from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('posts/', views.post_list, name='post_list'),
    path('create_post/', views.create_post, name='create_post'),

]
