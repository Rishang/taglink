from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.


class Category(models.Model):

    name = models.CharField(blank=False, max_length=100, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
            return reverse("user_links")


class Link(models.Model):

    url = models.URLField(blank=False)
    title = models.CharField(max_length=200)
    description = models.CharField(blank=True, max_length=500)
    imageUrl = models.URLField(blank=True, max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default="default", max_length=20, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return f"{self.user} | {self.url}"

    def get_absolute_url(self):
        return reverse("home-page")
