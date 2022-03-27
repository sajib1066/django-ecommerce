from django.contrib import admin
from .models import Category, Tag, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'date']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'date']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'is_draft', 'date']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
