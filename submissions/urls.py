from django.urls import path
from . import views

app_name = "submissions"

urlpatterns = [
    path('', views.user_suggestion, name="new_suggestion"),
    path('get-course/', views.get_department_id, name="getCourse")
]
