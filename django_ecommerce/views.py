from django.shortcuts import render
from shop.models import Product
from contact.forms import SubscriberForm


def home_page(request):
    products = Product.objects.all()[:8]
    forms = SubscriberForm()
    if request.method == 'POST':
        forms = SubscriberForm(request.POST)
        if forms.is_valid():
            forms.save()
    context = {
        'products': products,
        'forms': forms
    }
    return render(request, 'home.html', context)
