import math, datetime, random

from django.shortcuts import render
from django.views.generic.list import ListView

from common.misc_storage import MiscStorage

from .models import StatsEntry

class StatsView(ListView):
    model = StatsEntry
    paginate_by = 50
    template_name = 'player_online_stats/index.html'

    def get_context_data(self):
        extra_context = dict()

        extra_context['last_update'] = datetime.datetime.fromtimestamp(int(MiscStorage.get('player_online_stats.last_update', '0')))

        return super().get_context_data(**extra_context)

    def get_queryset(self):
        return self.model.objects.filter(time__gte=60).order_by('-time')  # pylint: disable=no-member