from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

# Form details for user while creating
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']