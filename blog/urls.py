from . import views
from django.urls import path

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path('entry/<int:pk>/', views.entry.as_view(), name='entry'),
    path('create_comment/<int:pk>/', views.create_comment, name='create_comment'),
    path('create_blog/', views.create_blog, name='create_blog'),
]