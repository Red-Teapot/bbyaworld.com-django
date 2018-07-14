import time, operator, math

from django.db import transaction
from django_cron import CronJobBase, Schedule
from common.misc_storage import MiscStorage
from common.mc import DynmapMarkup

from .models import ClanModel

class UpdateJob(CronJobBase):
    RUN_EVERY_MINS = 60 * 24 # Once per day

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=60)
    code = 'clans_cells.update_job'

    def do(self):
        mk = DynmapMarkup('http://play.bbyaworld.com:28565/tiles/_markers_/marker_world.json')
        mk.load()  
        data = mk.data
        cells = data['sets']['Clans2']['areas']

        clans = dict()

        for cell_id, cell_data in cells.items():
            cell_label = cell_data['label']

            clan_name_start = cell_label.find('(') + 1
            clan_name_end = cell_label.find(')')
            clan_name = cell_label[clan_name_start:clan_name_end]

            if clan_name == 'free':
                continue

            if clan_name in clans:
                clans[clan_name] += 1
            else:
                clans[clan_name] = 1
        
        clans_sorted = sorted(clans.items(), key=operator.itemgetter(1), reverse=True)

        order = 0

        print(clans_sorted)

        entries = list()

        for i in range(0, min([len(clans_sorted), 5])):
            clan = clans_sorted[i]

            entries += [ClanModel(order=order, name=clan[0], cell_count=clan[1], is_in_council=True)]
            order += 1
        
        last_clan = clans_sorted[len(entries) - 1]
        
        for i in range(5, len(clans_sorted)):
            clan = clans_sorted[i]
            is_in_council = False
            if clan[1] == last_clan[1]:
                is_in_council = True

            entries += [ClanModel(order=order, name=clan[0], cell_count=clan[1], is_in_council=is_in_council)]
            order += 1
        
        with transaction.atomic():
            ClanModel.objects.all().delete()  # pylint: disable=no-member
            ClanModel.objects.bulk_create(entries)  # pylint: disable=no-member