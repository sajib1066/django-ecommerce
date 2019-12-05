from django.shortcuts import render
from shop.models import Product

def home_page(request):
    products = Product.objects.all()[:8]
    context = {
        'products': products
    }
    return render(request, 'home.html', context)
