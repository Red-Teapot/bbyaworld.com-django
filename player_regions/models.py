from django.db import models

class PlayerRegion(models.Model):
    owner_nickname = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    label = models.CharField(max_length=128)
    area = models.FloatField()