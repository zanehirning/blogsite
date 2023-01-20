from django.shortcuts import render
from django.views import generic
from .models import Blog, Comments

# Create your views here.
def home(request):
    return render(request, "blog/home.html")

class entry(generic.DetailView):
    model = Blog
    template_name = "blog/entry.html"

    def get_queryset(self):
        return Blog.objects.order_by('-pub_date')