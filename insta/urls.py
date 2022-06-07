from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('home', views.home, name='home'),
    # # path('', views.sign_up, name='login'),
    # # path('sign-up', views.sign_up, name='sign-up'),
    # # path('profile/', views.profile, name='profile'),
    # # path('create-post', views.create_post, name='create_post'),
    # # path('author_profile/<str:username>', views.author_profile, name='author_profile'),
    # # path('edit_profile/', views.editProfile, name='edit_profile'),
    # # path('search/', views.search_profile, name='search'),
    # # path('profile/<str:username>/',views.profile,name='profile'),
    # # path('like-post/', views.like_post, name='like'),
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    