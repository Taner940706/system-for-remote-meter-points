from django.contrib import admin

from system_for_remote_meter_points.SIM.models import SIM


# Register your models here.
@admin.register(SIM)
class SIMAdmin(admin.ModelAdmin):
    pass
