import time, operator, math

from django.db import transaction
from django_cron import CronJobBase, Schedule
from common.misc_storage import MiscStorage
from common.mc import DynmapMarkup

from .models import PlayerRegion

class UpdateJob(CronJobBase):
    RUN_EVERY_MINS = 60 * 24 # Once per day

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=60)
    code = 'player_regions.update_job'

    def do(self):
        mk = DynmapMarkup('http://play.bbyaworld.com:28565/tiles/_markers_/marker_world.json')
        mk.load()  
        data = mk.data
        regions = data['sets']['players_houses']['areas']

        regions_objs = list()

        for name, reg in regions.items():
            label = reg['label']

            last_underscore = name.rfind('_')
            owner_nickname = name[0:last_underscore]
            try:
                reg_number = int(name[last_underscore + 1:])
            except:
                reg_number = -1

            x = reg['x']
            z = reg['z']
            point_count = min([len(x), len(z)])

            if point_count < 2:
                continue

            if point_count == 2:
                area = abs((x[1] - x[0]) * (z[1] - z[0]))
            else:
                area = 0
                for i in range(0, point_count):
                    next = i + 1 if i < point_count - 1 else 0

                    area += x[i] * z[next] - x[next] * z[i]
                area /= 2
                area = abs(area)

            regions_objs += [PlayerRegion(owner_nickname=owner_nickname, name=name, label=label, area=area)]
        
        with transaction.atomic():
            PlayerRegion.objects.all().delete()  # pylint: disable=no-member
            PlayerRegion.objects.bulk_create(regions_objs)  # pylint: disable=no-member

        MiscStorage.set('player_regions.last_update', str(int(time.time())))