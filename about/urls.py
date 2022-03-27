from django.urls import path
from .views import about_page


urlpatterns = [
    path('', about_page, name='about')
]
