from django.urls import path

from . import views

app_name = 'player_regions'

urlpatterns = [
    path('', views.index, name='index'),
]