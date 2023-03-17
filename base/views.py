from django.shortcuts import render


def home(request):
    context = {
        'title': "Home",
        'is_bootstrap': True,
    }
    return render(request, 'base.html', context)
