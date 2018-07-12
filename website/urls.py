from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rules', views.rules, name='rules'),
    path('newbie-info', views.newbie_info, name='newbie-info'),
    path('contacts', views.contacts, name='contacts'),
]