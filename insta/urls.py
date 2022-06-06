from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    PostListView,
    AuthorDetailView,
    PostCreateView,
    # PostUpdateView,
    # PostDeleteView
)

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.sign_up, name='login'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('profile/', views.profile, name='profile'),
    # path('create-post', views.create_post, name='create_post'),
    path('author_profile/', views.author_profile, name='author_profile'),
    path('edit_profile/', views.editProfile, name='edit_profile'),
    path('', PostListView.as_view(), name='insta-home'),
    path('user/<int:pk>/', AuthorDetailView.as_view(), name='author-profile'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    # path('post/new/', views.PostCreate, name='post_create'),
    # path('', views.index, name='insta-home'),
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    