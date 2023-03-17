from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from base import views as general_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', general_views.home, name="index"),
    path('register/', include('authenticator.urls', namespace="authenticator")),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
