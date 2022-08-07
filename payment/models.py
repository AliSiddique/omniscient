from django.db import models

class Pricing(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    stripe_price_id = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2,max_digits=5)
    currency = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.OneToOneField("user.User",on_delete=models.CASCADE)
    pricing = models.ForeignKey("payment.Pricing",on_delete=models.CASCADE,related_name='subscriptions')
    created = models.DateTimeField(auto_now_add=True)
    stripe_subscription_id = models.CharField(max_length=50)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email
