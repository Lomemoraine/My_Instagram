
from email.mime import image
import os
from django.test import TestCase
from .models import Profile, Image
from django.contrib.auth.models import User
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instagram.settings')
import django
django.setup()
# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='Joe')
        self.user.save()

        self.profile_test = Profile(id=1,  image='http://res.cloudinary.com/dim8pysls/image/upload/v1639001486/x3mgnqmbi73lten4ewzv.png', bio='test driven', user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)