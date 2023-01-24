from django.db import models
from django.utils import timezone
from django.urls import reverse

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=400)
    author = models.CharField(max_length=255)
    content = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    commenter = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    content = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse('blog:index')

