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
    # if request.method == "POST":
    #     u_form = UserUpdateForm(request.POST,instance=request.user)
    #     p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        
    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, f'You have Updated succesfully updated your profile')
    #         return redirect('profile')
    # else:
    #     u_form = UserUpdateForm(instance=request.user)
    #     p_form = ProfileUpdateForm(instance=request.user.profile)
    
    # context={
    #     'u_form':u_form,
    #     'p_form':p_form
    # }
    
  
    return render(request, 'registration/profile.html')
def editProfile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'You have succesfully updated your profile')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'registration/edit_profile.html',context)
    
    
      




