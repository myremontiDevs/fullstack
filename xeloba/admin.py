from django.contrib import admin
from .models import Adminlogin, Craftsman, Client

# Register your models here.
admin.site.register(Adminlogin)
admin.site.register(Craftsman)
admin.site.register(Client)