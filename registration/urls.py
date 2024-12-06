# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('get-started/', views.get_started, name='get_started'),
    path('success/', views.success, name='success'),
]