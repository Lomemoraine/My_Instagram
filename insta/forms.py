from django import forms
from .models import Image,Profile,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]
        
class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image','caption')
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo','bio')
class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder'] = 'Add a comment....'
    class Meta:
        model = Comment
        fields = ('comment',)

