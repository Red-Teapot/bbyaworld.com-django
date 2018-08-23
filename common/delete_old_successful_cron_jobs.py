from django_cron import CronJobBase, Schedule
from django_cron.models import CronJobLog


class Job(CronJobBase):
    RUN_EVERY_MINS = 60 * 24 # Once per day

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=60)
    code = 'common.delete_old_successful_cron_jobs'

    def do(self):
        job_types_raw = CronJobLog.objects.values_list('code')  # pylint: disable=no-member

        job_types = list()
        for job_type in job_types_raw:
            job_type = job_type[0]

            if job_type and job_type not in job_types:
                job_types.append(job_type)

        for job_type in job_types:
            job_logs = CronJobLog.objects.filter(code=job_type, is_success=True).order_by('-end_time')[:2].values('pk')  # pylint: disable=no-member

            if len(job_logs) <= 0:
                continue
            
            job_logs_list = [x['pk'] for x in list(job_logs)]

            to_delete = CronJobLog.objects.filter(code=job_type, is_success=True).exclude(pk__in=job_logs_list)  # pylint: disable=no-member

            to_delete.delete()
