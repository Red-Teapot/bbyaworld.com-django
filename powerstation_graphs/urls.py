from django.urls import path

from . import views

app_name = 'powerstation_graphs'

urlpatterns = [
    path('', views.index, name='index'),
    path('get-data/', views.get_data, name='get-data'),
]