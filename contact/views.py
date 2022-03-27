from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm


# Create your views here.
def contact_page(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Submitted.')
            return redirect('contact')
    context = {
        'form': form
    }
    return render(request, 'contact/contact.html', context)
