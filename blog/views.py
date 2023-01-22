from django.shortcuts import render
from django.views import generic
from .models import Blog, Comments
from .forms import BlogForm, CommentsForm

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

def create_comment(request):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = CommentsForm()
    return render(request, 'blog/create_comment.html', {'form': form})