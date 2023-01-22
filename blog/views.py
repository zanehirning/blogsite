from django.shortcuts import render, redirect, reverse
from django.views import generic
from .models import Blog, Comments
from .forms import BlogForm, CommentsForm
from datetime import datetime
from django.shortcuts import get_object_or_404

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
        return Blog.objects.order_by('-posted')

def create_comment(request, pk):
    print(request.POST)
    blog = get_object_or_404(Blog, pk=pk)
    print(blog.id)
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    if name and email and message:
        comment = Comments(blog=blog, commenter=name, email=email, content=message)
        comment.save()
        return redirect(reverse('entry', args=[pk]))
