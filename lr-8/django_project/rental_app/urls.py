# rental_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('project_info/', views.project_info, name='project_info'),
]
