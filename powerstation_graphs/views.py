from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse

from .scoreboard import Scoreboard
from .models import Measurement


def index(request):
    return render(request, 'powerstation_graphs/index.html')

def get_data(request):
    measurements = Measurement.objects.all()  # pylint: disable=no-member
    data = dict()

    for measurement in measurements:
        if str(measurement.type) not in Measurement.value_types_reverse:
            continue
        
        m_type = Measurement.value_types_reverse[str(measurement.type)]

        if m_type not in data:
            data[m_type] = {
                'dates': list(),
                'values': list(),
            }
        
        data[m_type]['dates'].append(measurement.datetime)
        data[m_type]['values'].append(measurement.value)
    
    return JsonResponse(data)