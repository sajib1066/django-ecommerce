from django.contrib import admin
from .models import Contact, Subscriber


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'date']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Subscriber)
