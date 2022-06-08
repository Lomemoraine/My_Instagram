from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [
   path('',views.index,name = 'index'),
   path('signup/',views.signup,name = 'signup'),
   path('profile/', views.profile, name='profile'),
   path('editProfile/', views.editProfile, name='editProfile'),
   path('createPost/', views.createPost, name='createPost'),
   path('like_image/<user_id>/<post_id>',views.like_image, name='like_image'),
   path('login/', auth_view.LoginView.as_view(template_name='registration/login.html'), name="login"),
   path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    