from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('images/', default="", blank=True, null=True)
    bio = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.bio
