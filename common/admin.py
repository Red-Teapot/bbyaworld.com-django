from django.contrib import admin

from . import models

class MiscStorageEntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.MiscStorageEntry, MiscStorageEntryAdmin)
