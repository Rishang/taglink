from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Profile
from django.http import HttpResponseRedirect
from django.urls import reverse


class createUser(UserCreationForm):
    class Meta:

        model = User
        fields = ("username", "email", "password1", "password2")

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.phone(self.cleaned_data.get('phone'))
    #     if commit:
    #         user.save()
    #     return user

class UserUpdateForm(forms.ModelForm):
    
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100,min_length=2)
    last_name = forms.CharField(max_length=100,min_length=2)
    
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'image',
        )
    def get_absolute_url(self):
        return HttpResponseRedirect(reverse('user_profile'))
