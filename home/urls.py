from django.urls import path
from . import views
from registration import views as registration_views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration', registration_views.get_started, name='get_started')
]