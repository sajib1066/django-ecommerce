from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'date']

admin.site.register(Contact, ContactAdmin)
