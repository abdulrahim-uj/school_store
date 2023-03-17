from django.urls import path
from . import views

app_name = "authenticator"

urlpatterns = [
    path('', views.signup, name="new_user"),
    path('login/', views.signin, name="existing_user"),
    path('authenticated/dashboard/', views.dashboard, name="my_dashboard"),
    path('logout/', views.signout, name="logout_user")
]
