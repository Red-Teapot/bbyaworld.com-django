from django.contrib import admin

from .models import PlayerRegion

class PlayerRegionAdmin(admin.ModelAdmin):
    pass

admin.site.register(PlayerRegion, PlayerRegionAdmin)
