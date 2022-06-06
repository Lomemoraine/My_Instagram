from email import message
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from insta.models import *
from .models import Post, Profile

# Create your views here.
# @login_required(login_url='/login')
def home(request):
    images = Post.objects.all()
    users = User.objects.exclude(id=request.user.id)
    return render(request,'general/index.html', {"images":images[::1],"users":users})
   
    

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
            messages.success(request, "Account created successfully")
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})
def login(request):
    return render(request, 'registration/login.html')

@login_required(login_url='/login')
def profile(request):
    context = {
        'posts': Post.objects.filter(post_owner=request.user).all()
    }
    return render(request, 'general/profile.html',context )


@login_required(login_url='/login')
def author_profile(request):
    context = {
        'posts': Post.objects.filter(post_owner=request.user).all(),
        
    }
    # if request.user == Post.objects.post.user:  
    return redirect('profile')
    # else:
    #     return render(request, 'users_app/not_user_profile.html',contex
    
@login_required
def editProfile(request):
    profile = Profile(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'general/edit_profile.html', context)





@login_required(login_url='/login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request,'general/create_post.html', {"form":form})

def search_profile(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request, 'general/search.html',{"message":message,"photos": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})