from django.contrib import admin

from system_for_remote_meter_points.SIM.models import SIM


# customize SIM for django admin
@admin.register(SIM)
class SIMAdmin(admin.ModelAdmin):
    list_display = ("sim_number", "gsm_number", "ip_address", "operator", "user", "created_date")
    list_filter = ("sim_number",)
    list_per_page = 10
    ordering = ('-created_date',)
