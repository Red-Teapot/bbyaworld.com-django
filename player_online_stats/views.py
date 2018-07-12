import math, datetime

from django.shortcuts import render
from django.http import HttpResponse

from .models import StatsEntry

def index(request):
    per_page = 50

    try:
        page = int(request.GET.get('p', 1))
    except ValueError:
        page = 1

    count = StatsEntry.objects.count()

    if page < 1:
        page = 1
    if page > math.ceil(count / per_page):
        page = math.ceil(count / per_page)

    entries = StatsEntry.objects.order_by('-time')[:4]

    context = {
        'total_count': count,
        'current_page': page,
        'players_stats': entries,
        'last_update': datetime.datetime(2012, 3, 12, 13, 34, 45),
    }

    return render(request, 'player_online_stats/index.html', context=context)