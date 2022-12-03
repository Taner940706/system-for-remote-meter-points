from django.contrib import admin

from system_for_remote_meter_points.meter_points.models import MeterPoint


# Register your models here.
@admin.register(MeterPoint)
class MeterPointAdmin(admin.ModelAdmin):
    pass