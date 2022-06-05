from email import message
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
@login_required(login_url='/login')
def home(request):
    return render(request, 'general/index.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            subject='Welcome to My Instagram'
            message=f'Hello {username}, browse with ease'
            from_email=settings.EMAIL_HOST_USER
            recepient_list=[email]
            send_mail(subject,message,from_email,recepient_list,fail_silently=False)
            form.save()
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})
def login(request):
    return render(request, 'registration/login.html')

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.post_owner=request.user
            post.save()
            return redirect('/home')
        else:
            form =PostForm()
        return render(request,'general/create_post.html',{'form': form})
        
    






