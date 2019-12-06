from django.shortcuts import render
from .models import Category, Product


def shop_page(request):
    category = Category.objects.all()
    products = Product.objects.filter(is_draft=False)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'shop/shop.html', context)

def product_details(request, product_id):
    product_details = Product.objects.get(id=product_id)
    context = {
        'product': product_details
    }
    return render(request, 'shop/product-details.html', context)
