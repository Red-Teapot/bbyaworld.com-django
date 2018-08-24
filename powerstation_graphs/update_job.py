from django.conf import settings
from django.utils import timezone
import datetime, time, math

from django_cron import CronJobBase, Schedule

from .scoreboard import Scoreboard
from .models import Measurement


STATS_PERIOD = 90  # 90 days

class UpdateJob(CronJobBase):
    RUN_EVERY_MINS = 60 * 24  # Once per day

    schedule = Schedule(RUN_EVERY_MINS, retry_after_failure_mins=60)
    code = 'powerstation_graphs.update_job'

    def do(self):
        # Delete old measurement records

        min_date = timezone.now() - datetime.timedelta(days=90)

        Measurement.objects.filter(datetime__lt=min_date).delete()  # pylint: disable=no-member

        # Add new measurement records
        rcon_settings = settings.SECRETS['mc']['rcon']

        with Scoreboard(rcon_settings['host'], rcon_settings['password'], port=rcon_settings['port']) as scoreboard:
            raw_wheat_pp_value = scoreboard.get_list_for_player('.PPWheat')['CustomID']
            raw_coal_pp_value = scoreboard.get_list_for_player('.PPCoal')['CustomID']
            raw_diamond_pp_value = scoreboard.get_list_for_player('.PPAlm')['CustomID']
            raw_exp_market_value = scoreboard.get_list_for_player('.expMarket')['CustomID']

            wheat_pp_value = raw_wheat_pp_value // 1000
            coal_pp_value = raw_coal_pp_value // 1000
            diamond_pp_value = raw_diamond_pp_value // 1000
            exp_market_value = raw_exp_market_value

            Measurement.objects.bulk_create([  # pylint: disable=no-member
                Measurement(type=Measurement.value_types['wheat_pp'], value=wheat_pp_value),
                Measurement(type=Measurement.value_types['coal_pp'], value=coal_pp_value),
                Measurement(type=Measurement.value_types['diamond_pp'], value=diamond_pp_value),
                Measurement(type=Measurement.value_types['exp_market'], value=exp_market_value),
            ])