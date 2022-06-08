from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Post,Comment


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture' ,'bio']
        
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','image_name','image_caption']
        exclude = ['image_owner','likes','comments']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 100%;',
                'placeholder': 'Comment'
                })
            }

