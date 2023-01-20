from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path('entry/<int:pk>/', views.entry.as_view(), name='entry'),
]