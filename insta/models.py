from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    bio = models.CharField(default="My Bio", max_length = 40)
    picture = CloudinaryField('images', default='https://res.cloudinary.com/dcfb3gqzg/image/upload/v1654542339/bclz5p1q2ch81qz9ukpz.jpg')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    
class Post(models.Model):
    image =CloudinaryField('images', blank=False)
    image_name = models.CharField(max_length=50,blank=True)
    image_caption = models.TextField(max_length=255,blank=True)
    image_owner = models.ForeignKey(Profile,null=True,on_delete=models.SET_NULL)
    likes = models.ManyToManyField(Profile, related_name = "likes", blank = True)
    comments = models.ManyToManyField(Profile, related_name = "comments", blank = True)
    
    def __str__(self):
        return f'{self.image_name} '
    
    def save_post(self):
        '''calling the inbuilt save method '''
        self.save()
        
class Comment(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    user_profile = models.ForeignKey(Profile,null=True,on_delete=models.SET_NULL)
    comment = models.CharField(blank=False, max_length=255)
    post_linked = models.ForeignKey(Post,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.comment
