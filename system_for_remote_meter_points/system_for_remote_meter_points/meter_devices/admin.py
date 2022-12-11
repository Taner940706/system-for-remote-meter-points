from django.contrib import admin

from system_for_remote_meter_points.meter_devices.models import MeterDevice


@admin.register(MeterDevice)
class MeterDeviceAdmin(admin.ModelAdmin):
    list_display = ("meter_device_number", "meter_device_type", "meter_device_read_cycle", "user")
    list_filter = ("meter_device_type",)
    search_fields = ("meter_device_number__contains",)
