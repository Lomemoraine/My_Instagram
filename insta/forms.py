from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from insta.models import Post, Profile



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]
        

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', ]
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','bio']

        
class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ["post_image", "post_caption"]
        exclude = ["likes", "pub_date", "comments", "post_owner"]
        