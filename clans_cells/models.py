from django.db import models

class ClanModel(models.Model):
    order = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    cell_count = models.IntegerField(default=0)
    is_in_council = models.BooleanField(default=False)
