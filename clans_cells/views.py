import math, datetime

from django.shortcuts import render
from django.views.generic.list import ListView

from common.misc_storage import MiscStorage

from .models import ClanModel

class IndexView(ListView):
    model = ClanModel
    template_name = 'clans_cells/index.html'
    extra_context = {
        'last_update': datetime.datetime.fromtimestamp(int(MiscStorage.get('clans_cells.last_update', '0'))),
    }

    def get_queryset(self):
        return self.model.objects.order_by('order')  # pylint: disable=no-member
