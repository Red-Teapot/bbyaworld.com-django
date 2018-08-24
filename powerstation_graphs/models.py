from django.db import models


class Measurement(models.Model):
    type = models.SmallIntegerField(default=-1, db_index=True)
    value = models.BigIntegerField(default=-1000)
    datetime = models.DateTimeField(auto_now=True, db_index=True)

    value_types = {
        'wheat_pp': 1,
        'coal_pp': 2,
        'diamond_pp': 3,
        'exp_market': 4,
    }