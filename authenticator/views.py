from django.contrib import messages, auth
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'messages': "User created, please login with your credentials",
                'title': "Sign in",
                'is_bootstrap': True,
            }
            return render(request, "auth/signin.html", context=context)
        else:
            messages.info(request, form.errors)
            return redirect('authenticator:new_user')
    else:
        form = UserRegistrationForm()
    context = {
        'title': "Registration",
        'is_bootstrap': True,
        'form': form,
    }
    return render(request, 'auth/registration.html', context)


def signin(request):
    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials!")
            return redirect('authenticator:existing_user')
    else:
        context = {
            'title': "Sign in",
            'is_bootstrap': True,
        }
    return render(request, 'auth/signin.html', context)


def signout(request):
    auth.logout(request)
    return redirect('/')
