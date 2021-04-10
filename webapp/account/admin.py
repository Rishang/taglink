from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile

# signup your models here.

admin.site.register(Profile)
