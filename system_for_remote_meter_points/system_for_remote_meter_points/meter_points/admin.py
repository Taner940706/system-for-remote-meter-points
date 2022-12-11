from django.contrib import admin

from system_for_remote_meter_points.meter_points.models import MeterPoint


@admin.register(MeterPoint)
class MeterPointAdmin(admin.ModelAdmin):
    list_display = ("mp_name", "meter_device", "regional_center", "user")
    list_filter = ("mp_name", "user")
    search_fields = ("mp_name__startswith",)
