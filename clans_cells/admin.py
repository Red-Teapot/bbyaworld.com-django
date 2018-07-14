from django.contrib import admin

from .models import ClanModel

class ClanModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(ClanModel, ClanModelAdmin)