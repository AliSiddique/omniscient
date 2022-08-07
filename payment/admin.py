from django.contrib import admin

from payment.models import Pricing, Subscription

# Register your models here.
admin.site.register(Pricing)
admin.site.register(Subscription)