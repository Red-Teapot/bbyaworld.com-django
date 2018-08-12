from django.db import models

class StatsEntry(models.Model):
    uuid = models.UUIDField(db_index=True, primary_key=True)
    nickname = models.CharField(max_length=64, db_index=True)
    time = models.IntegerField(db_index=True, default=0)
