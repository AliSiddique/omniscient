from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('content.urls')),
    path('people/',include('user.urls')),
    path('payments/',include('payment.urls')),
    path("__reload__/", include("django_browser_reload.urls")),


]
