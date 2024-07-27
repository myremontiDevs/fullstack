from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .models import Craftsman


urlpatterns = [
    path('admin', views.admlogin, name='admin'),
    path('login', views.login, name='login'),
    path('', views.index, name="index"),
    path('reg', views.reg, name="reg"),
    path('del', views.delete_user, name='delete_user'),
    path('addusers', views.add_user, name='add_user'),
    path('edit', views.edit_user, name='edit_user'),
    path('verifyuser', views.verify_user, name='edit_user'),
    path('myPage', views.index, name='space'),
    path('statistics', views.statistics, name='statistics'),
    path('onOff', views.onOffst, name='on_off')



]

