from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from base.functions import get_auto_id, generate_form_errors
from .forms import SuggestionForm
import json
from .models import Course, Suggestion


@login_required(login_url='authenticator:existing_user')
def user_suggestion(request):
    if request.method == "POST":
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.auto_id = get_auto_id(Suggestion)
            suggestion.creator = request.user
            suggestion.updater = request.user
            suggestion.save()
            # If submit & logout at the same time
            # auth.logout(request)
            # keep backup for sweat-alert
            response_data = {
                "status": "true",
                "title": "New User",
                "message": "Order confirmed.",
                "footer": '<a href="">Why do I have this issue?</a>',
                "redirect": 'false',
                "redirect_url": reverse('authenticator:my_dashboard')
            }
            # docstring with format & attached link
            message = """
            Order confirmed.
            <br />
            Click <a href='{url}'>here</a> to return back to home page.
            """
            url = reverse('authenticator:my_dashboard')
            messages.info(request, mark_safe(message.format(url=url)))
            return redirect('submissions:new_suggestion')
        else:
            messages.info(request, form.errors)
            return redirect('submissions:new_suggestion')
        #     message = generate_form_errors(form, formset=False)
        #     response_data = {
        #         "status": "false",
        #         "stable": "true",
        #         "title": "Form validation error",
        #         "message": message[0].messages[0]
        #     }
        # return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SuggestionForm()
    context = {
        'title': "user suggestions",
        'is_bootstrap': True,
        'form': form,
    }
    return render(request, 'submissions/submission-form.html', context)


@login_required(login_url='authenticator:existing_user')
def get_department_id(request):
    data = json.loads(request.body)
    department_pk = data["id"]
    courses = Course.objects.filter(department__id=department_pk)
    return JsonResponse(list(courses.values("id", "course_name")), safe=False)
