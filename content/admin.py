from django.contrib import admin
from .models import Article, Comment, Contact
# Register your models here.
admin.site.register(Article)
admin.site.register(Contact)
admin.site.register(Comment)