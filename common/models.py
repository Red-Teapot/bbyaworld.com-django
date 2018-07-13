from django.db import models

class MiscStorageEntry(models.Model):
    key = models.CharField(max_length=64, db_index=True, primary_key=True)
    value = models.CharField(max_length=256)