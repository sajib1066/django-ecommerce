from django.urls import path
from .views import signin_page
from .views import signup_page


urlpatterns = [
    path('', signin_page, name='signin'),
    path('\signup', signup_page, name='signup')
]