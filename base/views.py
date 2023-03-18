from django.shortcuts import render
from submissions.models import Department


def home(request):
    context = {
        'title': "Home",
        'is_bootstrap': True,
    }
    return render(request, 'home/home.html', context)
