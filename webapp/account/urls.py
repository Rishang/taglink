from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", views.register, name="register_page"),
    path("signin/", auth_views.LoginView.as_view(), name="login_page"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/<slug:slug>", views.userProfile.as_view(), name="user_profile"),
    path("profile/<slug:slug>/edit", views.userProfile.as_view(), name="edit_profile"),
    path("profile/<slug:slug>/delete", views.userProfile.as_view(), name="delete_profile"),
]
