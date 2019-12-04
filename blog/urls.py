from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_page, name='blog'),
    path('details/<post_id>', views.post_details, name='post-details')
]
