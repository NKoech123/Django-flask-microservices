
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nomad.urls', namespace='nomad')),
    path('api/', include('nomad_api.urls', namespace='nomad_api')),
]
