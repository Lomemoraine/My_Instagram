from email import message
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Profile
# Create your views here.
def index(request):
   
    
    return render(request,'index.html')
def signup(request):
    if request.method == "POST":
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully Proceed to login')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'registration/signup.html', {'form': form})
@login_required()
def profile(request):
    
  
    return render(request, 'registration/profile.html')

      




