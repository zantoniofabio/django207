from django.urls import path

from . import views

app_name = 'home'  # namespace para o app

urlpatterns = [
    path("", views.home, name='home'),
]
