from django.urls import path

from . import views

app_name='server_status'

urlpatterns = [
    path('', views.status, name='index'),
]