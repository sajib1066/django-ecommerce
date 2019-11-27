from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_page, name='blog')
]
