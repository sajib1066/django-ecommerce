from django.shortcuts import render
from django.db.models import Count

from .models import Category, Tag, Post


def blog_page(request):
    post = Post.objects.filter(is_draft=False)
    category = Category.objects.all().annotate(
        number_of_posts=Count('post')
    ).order_by('-number_of_posts', 'name')
    tag = Tag.objects.all()
    recent_post = Post.objects.filter(is_draft=False).order_by('-date')[:3]
    context = {
        'posts': post,
        'categories': category,
        'tags': tag,
        'recent_posts': recent_post
    }
    return render(request, 'blog/blog.html', context)


def post_details(request, post_id):
    post = Post.objects.get(id=post_id)
    category = Category.objects.all().annotate(
        number_of_posts=Count('post')
    ).order_by('-number_of_posts', 'name')
    tag = Tag.objects.all()
    recent_post = Post.objects.filter(is_draft=False).order_by('-date')[:3]
    context = {
        'post': post,
        'categories': category,
        'tags': tag,
        'recent_posts': recent_post
    }
    return render(request, 'blog/post-details.html', context)


def post_by_category(request, ctg_name):
    ctg = Category.objects.get(name=ctg_name)
    post = Post.objects.filter(category=ctg)
    category = Category.objects.all().annotate(
        number_of_posts=Count('post')
    ).order_by('-number_of_posts', 'name')
    tag = Tag.objects.all()
    recent_post = Post.objects.filter(is_draft=False).order_by('-date')[:3]
    context = {
        'posts': post,
        'categories': category,
        'tags': tag,
        'recent_posts': recent_post
    }
    return render(request, 'blog/post-by-category.html', context)
