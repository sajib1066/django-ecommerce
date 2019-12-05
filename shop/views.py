from django.shortcuts import render
from .models import Product


def shop_page(request):
    return render(request, 'shop/shop.html')

def product_details(request, product_id):
    product_details = Product.objects.get(id=product_id)
    context = {
        'product': product_details
    }
    return render(request, 'shop/product-details.html', context)
