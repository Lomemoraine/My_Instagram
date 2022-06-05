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

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def profile(request,username):
    user_name = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user_name.id)

    user_posts = Post.objects.filter(post_owner=user_name.id)
    # post_comments = Comment.objects.all()
    
    context={
        'user_name':user_name,
        'user_profile':user_profile,
        'user_posts':user_posts,
        # 'post_comments':post_comments
    }
    # return render(request,'profile.html',context=context)
    return render(request, 'general/profile.html',context=context )

@login_required(login_url='/login')
def author_profile(request):
    context = {
        'posts': Post.objects.filter(post_owner=request.user).all(),
        
    }
    # if request.user == Post.objects.post.user:  
    return redirect('profile')
    # else:

@login_required(login_url='/login')
def editProfile(request):
    # profile = Profile(user=request.user)

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
        
    






