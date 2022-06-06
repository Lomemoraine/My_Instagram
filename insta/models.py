from datetime import timezone
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.
class Profile(models.Model):
    image = CloudinaryField('images', default="", blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, default="Share more about yourself", blank=True)
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    @classmethod
    def profile(cls):
        profiles = cls.objects.all()
        return profiles
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    def save_profile(self):
        self.user
    def __str__(self):
        return self.name
    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

    def __str__(self):
            return f'{self.user} Profile'
        
class Post(models.Model):
    post_image = CloudinaryField('post_images',)
    # post_name = models.CharField(max_length=50,blank=True)
    post_caption = models.TextField(max_length=500,blank=True)
    post_owner = models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name='images')
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.BigIntegerField(default=0)
    comments = models.CharField(max_length=200, null=True, blank=True)
   

    def __str__(self):
        return self.post_caption
  
    def save_post(self):
        self.save()
    
    def get_absolute_url(self):
        return reverse('insta-home')

    
class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'
    
class Comment(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    user_comment = models.CharField(blank=False, max_length=255)
    post_associated = models.ForeignKey(Post,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.user_comment
    
class Like(models.Model):
    vote = models.IntegerField()
    user_vote = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    post_voted = models.OneToOneField(Post,null=True,on_delete=models.CASCADE)
     