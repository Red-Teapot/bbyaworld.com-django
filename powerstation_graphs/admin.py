from django.contrib import admin

from . import models


class MeasurementAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Measurement, MeasurementAdmin)
