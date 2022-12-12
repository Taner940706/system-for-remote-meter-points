from django.contrib import admin

from system_for_remote_meter_points.modems.models import Modem


@admin.register(Modem)
class ModemAdmin(admin.ModelAdmin):
    list_display = ("modem_number", "sim", "user", "created_date")
    list_filter = ("modem_number",)
    list_per_page = 10
    ordering = ('-created_date',)
