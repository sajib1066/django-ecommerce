from django.contrib import admin
from .models import AuthorProfile


class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email', 'gender', 'date']


admin.site.register(AuthorProfile, AuthorProfileAdmin)
