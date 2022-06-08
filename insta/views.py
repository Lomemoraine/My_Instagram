from email import message
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Like, Profile

# Create your views here.
# @login_required()
# def index(request):
#     comment_form = CommentForm()
#     all_posts = Post.objects.all().order_by('id').reverse()
    
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             post_linked_id = request.POST.get('post_linked')
            
#             user = request.user
#             user_profile = Profile.objects.get(user=user.id)
#             post_linked = Post.objects.get(id=post_linked_id)
#             comment = comment_form.cleaned_data['comment']
            
#             comment = Comment(
#                 user=user,
#                 user_profile=user_profile,
#                 comment=comment,
#                 post_linked=post_linked
#                 )
#             comment.save()
#             return redirect('index')
#         context={
        
#         # 'post_comments':post_comments,
#         'comment_form':comment_form,
#         # 'all_votes':all_votes
#     }
   
#     return render(request,'index.html',{"all_posts":all_posts[::1]},context=context)
@login_required()
def index(request):
    all_posts = Post.objects.all().order_by('id').reverse()
    post_comments = Comment.objects.all()
    all_votes = Like.objects.all()
  
    

    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            post_linked_id = request.POST.get('post_linked')

            user = request.user
            user_profile = Profile.objects.get(user=user.id)
            post_linked = Post.objects.get(id=post_linked_id)
            comment = comment_form.cleaned_data['comment']

            comment = Comment(
                user=user,
                user_profile=user_profile,
                comment=comment,
                post_linked=post_linked
                )
            comment.save()
            return redirect('index')

    context={
        'all_posts':all_posts,
        'all_votes':all_votes,
        'comment_form':comment_form,
        'post_comments':post_comments,
        
    }
    return render(request,'index.html',context=context)

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

@login_required()
def like_image(request,user_id,post_id):
    user_profile=User.objects.get(id=user_id)

    post_voted = Post.objects.get(id=post_id)
    profile_vote = Profile.objects.get(user=user_profile)

    print(post_voted,profile_vote)
    new_like = Like(
        profile_vote=profile_vote,
        post_voted=post_voted
    )
    new_like.save_like()

    return redirect('index')
        


    
      




