import math, datetime

from django.shortcuts import render
from django.views.generic.list import ListView

from .models import StatsEntry

class StatsView(ListView):
    model = StatsEntry
    paginate_by = 50
    template_name = 'player_online_stats/index.html'
    extra_context = {
        'last_update': datetime.datetime(2012, 2, 16, 15, 23, 35),
    }

    def get_queryset(self):
        return self.model.objects.filter(time__gte=60).order_by('-time')  # pylint: disable=no-member