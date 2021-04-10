from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListAllUserLinks.as_view(), name="home-page"),
    path("add_link/", views.createLink.as_view(), name="add_link"),
    path("add_category/", views.createCategory.as_view(), name="add_categoty"),
    path("my_links/", views.listLinksAndCategory.as_view(), name="user_links"),
    path("my_links/<int:pk>/delete/", views.deleteLink.as_view(), name="user_links"),
]
