import datetime

from django.shortcuts import render

from .models import PlayerRegion
from common.misc_storage import MiscStorage

def region_insort(regions, region, sort='area', reverse=True):
    i = 0
    loop_finished = False

    for i in range(0, len(regions)):
        if not reverse and regions[i][sort] > region[sort]:
            break
        if reverse and regions[i][sort] < region[sort]:
            break
        
        if i == len(regions) - 1:
            loop_finished = True

    print(i)
    
    if loop_finished:
        regions += [region]
    else:
        regions[i:i] = [region]

    return regions

def index(request):
    sort_by = request.GET.get('sort', default='area')
    sort_dir = request.GET.get('dir', default='desc')

    objects_raw = PlayerRegion.objects.all()  # pylint: disable=no-member

    sort_field = 'label' if sort_by == 'nickname' else 'area'
    reverse = (sort_dir != 'asc')

    regions = dict()

    for reg in objects_raw:
        owner = reg.owner_nickname

        if owner in regions:
            regions[owner]['total_area'] += reg.area
            region_insort(regions[owner]['areas'], {
                    'label': reg.label,
                    'area': reg.area,
                }, sort=sort_field, reverse=reverse)
        else:
            regions[owner] = {
                'total_area': reg.area,
                'areas': [{
                    'label': reg.label,
                    'area': reg.area,
                }],
            }

    regions_sorted = sorted(regions.items(), 
        key=lambda x: x[0] if sort_by == 'nickname' else x[1]['total_area'], 
        reverse=(sort_dir != 'asc'))

    context = {
        'sort': sort_by,
        'sort_dir': sort_dir,
        'list': regions_sorted,
        'last_update': datetime.datetime.fromtimestamp(int(MiscStorage.get('player_regions.last_update', '0'))),
    }

    return render(request, 'player_regions/index.html', context=context)