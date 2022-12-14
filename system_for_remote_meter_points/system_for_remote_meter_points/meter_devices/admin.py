from django.contrib import admin

from system_for_remote_meter_points.meter_devices.models import MeterDevice


# customize meter devices for django admin
@admin.register(MeterDevice)
class MeterDeviceAdmin(admin.ModelAdmin):
    list_display = ("meter_device_number", "meter_device_type", "meter_device_read_cycle", "user")
    list_filter = ("meter_device_type",)
    list_per_page = 10
    search_fields = ("meter_device_number__contains",)
