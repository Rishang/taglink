from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic import CreateView, ListView, DetailView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Link, Category

from .forms import addLink

# Create your views here.
class createCategory(LoginRequiredMixin, CreateView):
    model = Category
    fields = ("name",)
    template_name = "category/add_category.html"

    login_url = reverse_lazy("login_page")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class createLink(LoginRequiredMixin, CreateView):
    
    model = Link
    fields =  ("url", "title", "description", "imageUrl", "category", "tags")
    
    def get(self, request, *args, **kwargs):
            context = {'form': addLink(user_id=self.request.user.id)}
            return render(request, 'links/link_form.html', context)
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class listLinksAndCategory(LoginRequiredMixin, ListView):

    template_name = "links/user_links.html"
    context_object_name = "links"
    login_url = reverse_lazy("login_page")


    def get_queryset(self):
        user = User.objects.get(username=self.request.user)
        user_links = user.link_set.all()
        user_category = user.category_set.all()
        return {"user_links": user_links, "user_category": user_category}


class ListAllUserLinks(LoginRequiredMixin, ListView):

    model = Link
    context_object_name = "links"
    template_name = "home/all_links.html"
    login_url = reverse_lazy("login_page")


class deleteLink(LoginRequiredMixin, UserPassesTestMixin,DeleteView):

    model = Link
    success_url = reverse_lazy('user_links')
    login_url = reverse_lazy("login_page")

    def test_func(self):

        link = self.get_object()
        if self.request.user == link.user:
            return True
        else:
            return False
