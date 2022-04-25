
from django.urls import path
from django.views.generic import TemplateView

app_name = 'nomad'
urlpatterns = [
    path('', TemplateView.as_view(template_name ='nomad/index.html')),
    
]
