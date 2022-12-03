from django.contrib import admin

from system_for_remote_meter_points.meter_devices.models import MeterDevice


# Register your models here.
@admin.register(MeterDevice)
class MeterDeviceAdmin(admin.ModelAdmin):
    pass