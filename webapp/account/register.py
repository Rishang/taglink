from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


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
