from django import forms
from .models import Blog, Comments
from datetime import datetime

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('image', 'title', 'author', 'content', 'posted')
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'posted': forms.DateInput(attrs={'class': 'form-control'}),
        }

class CommentsForm(forms.ModelForm):
    class Meta:
        model=Comments

        fields = ('commenter', 'email', 'content' )
        widgets = {
            'commenter': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }