from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
import stripe
from payment.models import Pricing, Subscription
# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=50,blank=True ,null=True)
    email = models.EmailField()
    stripe_customer_id = models.CharField(max_length=50)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15,blank=True,null=True)
    image = models.ImageField(blank=True,null=True,default='images/default.jpeg')
    bio = models.TextField(max_length=500,blank=True,null=True,default=None)
    course = models.CharField(max_length=20,blank=True,null=True)
    uni = models.CharField(max_length=100,blank=True,null=True,default=None)
    slug= models.SlugField(max_length=30,unique=True)
    twitter = models.CharField(max_length=40,blank=True,null=True)
    website = models.URLField(blank=True,null=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_writer = models.BooleanField(default=False)
    views = models.BigIntegerField(default=0)
    
    def __str__(self) -> str:
         return self.user.username


    class Meta:
        ordering = ['-joined']




def user_profile_create(instance,created,sender,**kwargs):
    if created:
            user = instance
            Profile.objects.create(
                user=user,
                name = user.name,
                username = user.username,
                email=user.email,
                slug=user.username
            )
            free_pricing = Pricing.objects.get(name='Free')
            subscription  = Subscription.objects.create(
            user=instance,
            pricing=free_pricing)
            stripe_customer = stripe.Customer.create(
                email=instance.email
            )
            stripe_subscription = stripe.Subscription.create(
            customer=stripe_customer["id"],
            items=[{'price': 'price_1LZFnuLF9bIFNtJzL7br6j0h'}],
            trial_period_days = 7
                )
            print(stripe_subscription)    
            subscription.status = stripe_subscription["status"]
            subscription.stripe_subscription_id = stripe_subscription["id"]
            subscription.save()
            subscription.user.stripe_customer_id = stripe_customer["id"]
            subscription.user.save()
post_save.connect(user_profile_create,sender=User,dispatch_uid="user_profile_create")


def updateUser(sender,instance,created,**kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.name  = profile.name
        user.email = profile.email
        user.save()

post_save.connect(updateUser,sender=Profile)    