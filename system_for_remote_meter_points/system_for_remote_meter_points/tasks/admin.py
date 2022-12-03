from django.contrib import admin

from system_for_remote_meter_points.tasks.models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("mp_name", "operation", "result_operation", "meter_device", "username", "created_date")
    list_filter = ("operation", "result_operation")
    search_fields = ("mp_name__contains",)
    ordering = ('-created_date',)