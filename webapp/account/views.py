from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ValidationError
from .register import createUser

from django.contrib.auth.models import User
from django.views.generic import ListView

# Create your views here.


class userProfile(ListView):

    template_name = "profile/index.html"

    context_object_name = "slugUser"

    def get_queryset(self):

        user = User.objects.get(username=self.kwargs["slug"])
        user_profile = user.profile
        user_links = user.link_set.all()

        return {"profile": user_profile, "links": user_links}


def register(request):

    newUser = createUser(request.POST or None)
    if newUser.is_valid():
        newUser.save()
        username = newUser.cleaned_data.get("username")
        messages.info(request, f"sucess {username}")

        return redirect("login_page")

    return render(request, "registration/register.html", {"signup": newUser})
