from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    image = CloudinaryField('images/', default="", blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, default="Share more about yourself", blank=True)

def __str__(self):
        return f'{self.user.username} Profile'

class Post(models.Model):
    post_image = CloudinaryField('images/', default="", blank=True, null=True)
    image_name = models.CharField(max_length=50,blank=True)
    image_caption = models.TextField(max_length=500,blank=True)
    image_owner = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name
       