from django.contrib import admin

from . import models

class StatsEntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.StatsEntry, StatsEntryAdmin)
