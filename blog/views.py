from django.shortcuts import render
from .models import Category, Tag, Post

def blog_page(request):
    post = Post.objects.filter(is_draft=False)
    category = Category.objects.all()
    tag = Tag.objects.all()
    recent_post = Post.objects.filter(is_draft=False).order_by('-date')[:3]
    context = {
        'posts': post,
        'categories': category,
        'tags': tag,
        'recent_posts': recent_post
    }
    return render(request, 'blog/blog.html', context)
