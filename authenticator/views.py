import json
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from base.functions import generate_form_errors
from .forms import UserRegistrationForm


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #
            response_data = {
                "status": "true",
                "title": "New User",
                "message": "New user Successfully Created.",
                "redirect": 'true',
                "redirect_url": reverse('authenticator:existing_user')
            }
        else:
            message = generate_form_errors(form, formset=False)
            response_data = {
                "status": "false",
                "stable": "true",
                "title": "Form validation error",
                "message": message[0].messages[0]
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = UserRegistrationForm()
    context = {
        'title': "Registration",
        'is_bootstrap': True,
        'form': form,
        "redirect": True,
    }
    return render(request, 'auth/registration.html', context)


def signin(request):
    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            response_data = {
                "status": "true",
                "title": "User",
                "message": "User successfully login.",
                "redirect": 'true',
                "redirect_url": reverse('authenticator:my_dashboard')
            }
        else:
            response_data = {
                "status": "false",
                "stable": "true",
                "title": "Form validation error",
                "message": "Invalid credentials."
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            'title': "Sign in",
            'is_bootstrap': True,
            "redirect": True,
        }
    return render(request, 'auth/signin.html', context)


@login_required(login_url='authenticator:existing_user')
def dashboard(request):
    username = request.user.username
    context = {
        'title': username + "\'s home",
        'is_bootstrap': True,
        "redirect": True,
    }
    return render(request, 'dashboard/user-home.html', context)


@login_required(login_url='authenticator:existing_user')
def signout(request):
    auth.logout(request)
    response_data = {
        "status": "true",
        "title": "User",
        "message": "User successfully logout.",
        "redirect": 'true',
        "redirect_url": reverse('index')
    }
    return redirect('/')
