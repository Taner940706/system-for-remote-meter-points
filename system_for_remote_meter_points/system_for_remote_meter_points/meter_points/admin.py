from django.contrib import admin

from system_for_remote_meter_points.meter_points.models import MeterPoint


# customize meter point for django admin
@admin.register(MeterPoint)
class MeterPointAdmin(admin.ModelAdmin):
    list_display = ("mp_name", "meter_device", "regional_center", "user")
    list_filter = ("mp_name", "user")
    list_per_page = 10
    search_fields = ("mp_name__startswith",)
