from django.urls import path
from django.views.decorators.cache import never_cache

from . import views

app_name='player_online_stats'

urlpatterns = [
    path('', never_cache(views.StatsView.as_view()), name='index'),
]