from . import views
from django.urls import path

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path('entry/<int:pk>/', views.entry.as_view(), name='entry'),
]