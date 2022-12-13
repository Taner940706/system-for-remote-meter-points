from django.contrib import admin

from system_for_remote_meter_points.tasks.models import Task


# customize task for django admin
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("mp_name", "operation", "result_operation", "meter_device", "username", "created_date")
    list_filter = ("operation", "result_operation")
    search_fields = ("mp_name__contains",)
    list_per_page = 10
    ordering = ('-created_date',)
