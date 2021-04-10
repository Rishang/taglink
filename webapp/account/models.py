from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Profile(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_images", null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    def get_absolute_url(self):
        return reverse("profile")
