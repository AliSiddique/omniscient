from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(blank=False,null=False)
    stripe_customer_id = models.CharField(max_length=50)
    is_writer = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    image = models.ImageField(blank=True,null=True)
    bio = models.TextField(max_length=500,blank=True,null=True)
    uni = models.CharField(max_length=100,blank=True,null=True)
    slug= models.SlugField(max_length=30, blank=True,  null=True,unique=True)
    twitter = models.CharField(max_length=40)
    website = models.URLField()


