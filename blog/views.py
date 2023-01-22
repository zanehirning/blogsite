from django.shortcuts import render
from django.views import generic
from .models import Blog, Comments

# Create your views here.
class HomeView(generic.ListView):
    template_name="blog/home.html"
    context = "blog_list"
    def get_queryset(self):
        return Blog.objects.order_by('-posted')

class entry(generic.DetailView):
    model = Blog
    template_name = "blog/entry.html"

    def get_queryset(self):
        return Blog.objects.order_by('-pub_date')