from django.contrib import admin
from .models import Appartment, Comment, Favorites

# Register your models here.
admin.site.register([Appartment, Comment, Favorites])