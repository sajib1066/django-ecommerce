from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from account.forms import LoginForm, RegistrationForm
from django.contrib.auth import get_user_model

User = get_user_model()


def registration_view(request):
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')

            user = form.save()
            message = f"{firstname} {lastname} has been created"
            messages.success(request, message)
            return redirect('login')
        else:
            message = f'Error processing form'
            messages.error(request, message)
    return render(request, 'accounts/signup.html', {'form':form})


def login_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('home')

    form = LoginForm()
    print(form)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email_or_username = form.cleaned_data.get('email_or_username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email_or_username, password=password)
            login(request, user)
            messages.success(request, 'Successfully Logged In')
            return redirect('home')
    context = {
        'form': form
    }
    template_name = 'accounts/login.html'
    return render(request, template_name, context)


def logout_view(request, *args, **kwargs):
    logout(request)
    message = 'You have successfully logged out'
    messages.success(request, message)
    return redirect('accounts:login')