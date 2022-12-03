from django.contrib import admin

from system_for_remote_meter_points.modems.models import Modem


# Register your models here.
@admin.register(Modem)
class ModemAdmin(admin.ModelAdmin):
    list_display = ("modem_number", "sim", "user", "created_date")
    list_filter = ("modem_number",)
    ordering = ('-created_date',)