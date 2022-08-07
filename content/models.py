from email import message
from django.db import models

from user.models import Profile
from payment.models import Pricing
# Create your models here.
CHOICES =(
    ("Ec", "Economy"),
    ("FI", "Finance"),
    ("Po", "Politics"),
    ("TE", "Technology"),
    ("Sp", "Sports"),
    ("uni","University"),
    ("Me","Media")
)
class Article(models.Model):
    writer=models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1500)
    slug=models.SlugField(max_length=30, blank=True,  null=True,unique=True)
    favourites = models.ManyToManyField(Profile,related_name='favourites',default=None,blank=True)
    views = models.BigIntegerField()
    pricing_tiers = models.ManyToManyField(Pricing,blank=True)
    image = models.ImageField()
    category = models.CharField(choices=CHOICES,max_length=100,blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)



    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.CharField(max_length=500,blank=True,null=True)
    post = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments',blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)





class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=300)