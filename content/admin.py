from django.contrib import admin
from .models import Article, BecomeWriter, Comment, Contact
# Register your models here.
admin.site.register(Article)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(BecomeWriter)