from django.contrib import admin

from system_for_remote_meter_points.modems.models import Modem


# Register your models here.
@admin.register(Modem)
class ModemAdmin(admin.ModelAdmin):
    pass