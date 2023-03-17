from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import render

from base.functions import get_auto_id
from .forms import SuggestionForm
import json
from .models import Course, Suggestion


def user_suggestion(request):
    if request.method == "POST":
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.auto_id = get_auto_id(Suggestion)
            suggestion.creator = request.user
            suggestion.updater = request.user
            suggestion.save()
            auth.logout(request)
        else:
            print(form.errors)
    else:
        form = SuggestionForm()
    context = {
        'title': "user suggestions",
        'is_bootstrap': True,
        'form': form,
    }
    return render(request, 'submissions/submission-form.html', context)


def get_department_id(request):
    data = json.loads(request.body)
    department_pk = data["id"]
    courses = Course.objects.filter(department__id=department_pk)
    return JsonResponse(list(courses.values("id", "course_name")), safe=False)
