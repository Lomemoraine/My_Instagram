from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('create-post', views.create_post, name='create_post'),
    path('profile/', views.profile, name='profile'),
    path('author_profile/', views.author_profile, name='author_profile'),
    path('edit_profile/', views.editProfile, name='edit_profile'),

   
 
]