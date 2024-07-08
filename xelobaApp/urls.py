from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    path('', include('xeloba.urls')),
    path('db/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.CRAFTSIMGS, document_root=settings.MEDIA_ROOT)