from django.shortcuts import render

# Create your views here.
def shop_page(request):
    return render(request, 'shop/shop.html')

def product_details(request, product_id):
    return render(request, 'shop/product-details.html')
