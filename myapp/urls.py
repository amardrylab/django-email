from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.EmailView.as_view()),
    path('success', TemplateView.as_view(template_name='success.html')),
]
