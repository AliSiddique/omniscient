from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('content.urls')),
    path('people/',include('user.urls')),
    path('payments/',include('payment.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('tinymce/', include('tinymce.urls')),



]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

