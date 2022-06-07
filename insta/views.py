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
@login_required()
def index(request):
    all_posts = Post.objects.all().order_by('id').reverse()
   
    
    return render(request,'index.html',{"all_posts":all_posts[::1]})
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
@login_required()
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
def createPost(request):
    c_form = PostCreateForm()

    if request.method == "POST":
        c_form=PostCreateForm(request.POST,request.FILES)
        if c_form.is_valid():
            user=request.user
            
            image = c_form.cleaned_data.get('image')
            image_name = c_form.cleaned_data.get('image_name')
            image_caption  = c_form.cleaned_data.get('image_caption')
            image_owner = Profile.objects.get(user=user.id)
            
            new_post = Post(
                image=image,
                image_name=image_name,
                image_caption=image_caption,
                image_owner=image_owner
            )
            new_post.save_post()
            return redirect('index')
        else:
            c_form = PostCreateForm()
       

    context={
        'c_form':c_form
    }
    return render(request,'create_post.html',context=context)
        


    
      




