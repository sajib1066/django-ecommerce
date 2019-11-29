from django.shortcuts import render

# Create your views here.
def shop_page(request):
    return render(request, 'shop/shop.html')
