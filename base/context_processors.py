import datetime


def base_context(request):
    return {
        'app_title': "School Store",
        'today': datetime.date.today(),
        'domain': request.META['HTTP_HOST'],
    }
