# posts/urls.py
from django.urls import path

from . import views


urlpatterns = [
    # Главная страница
    path('', views.index),
    # посты по группам, ждут slug
    path('group/<slug:slug>/', views.group_posts)
]
