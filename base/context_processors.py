import datetime

from submissions.models import Department


def base_context(request):
    departments = Department.objects.filter(is_deleted=False, is_visible=True).order_by('department_name')
    return {
        'app_title': "School Store",
        'today': datetime.date.today(),
        'domain': request.META['HTTP_HOST'],
        'departments': departments,
    }
