import time

from django.db import transaction
from django_cron import CronJobBase, Schedule
from mcstatus import MinecraftServer
from common.misc_storage import MiscStorage

from .models import StatsEntry


def strip_dashes(value: str) -> str:
    return value.replace('-', '')

class UpdateJob(CronJobBase):
    RUN_EVERY_MINS = 2 # Once per 2 minutes
    RUN_TOLERANCE_SECONDS = 5

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, run_tolerance_seconds=RUN_TOLERANCE_SECONDS)
    code = 'player_online_stats.update_job'

    def do(self):
        try:
            mc_server = MinecraftServer.lookup('play.bbyaworld.com:25565')
            status = mc_server.status()
        except:
            raise Exception('Failed to get Minecraft server status')
        
        players = dict()

        # mcstatus actually returns None if there are no players on the server
        if status.players.sample:
            for p in status.players.sample:
                players[strip_dashes(p.id)] = p.name
        
        with transaction.atomic():
            # Process players that are already in DB
            entries = StatsEntry.objects.filter(uuid__in=players.keys())  # pylint: disable=no-member
            for e in entries:
                nickname = players.pop(strip_dashes(str(e.uuid)))

                e.time += self.RUN_EVERY_MINS
                if e.nickname is not nickname:
                    e.nickname = nickname
                
                e.save()
            
            # Add other players
            entries = list()
            for uuid, name in players.items():
                entries += [StatsEntry(nickname=name, uuid=uuid, time=self.RUN_EVERY_MINS)]
            
            StatsEntry.objects.bulk_create(entries)  # pylint: disable=no-member

        MiscStorage.set('player_online_stats.last_update', str(int(time.time())))