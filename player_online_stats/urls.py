from django.urls import path

from . import views

app_name='player_online_stats'

urlpatterns = [
    path('', views.index, name='index'),
]