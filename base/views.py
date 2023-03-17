from django.shortcuts import render
from submissions.models import Department


def home(request):
    departments = Department.objects.filter(is_deleted=False, is_visible=True).order_by('department_name')
    context = {
        'title': "Home",
        'is_bootstrap': True,
        'departments': departments,
    }
    return render(request, 'home/home.html', context)
