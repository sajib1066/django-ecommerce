from django.shortcuts import render


# Create your views here.
def cart_page(request):
    return render(request, 'cart/cart.html')


def checkout(request):
    return render(request, 'cart/checkout.html')
