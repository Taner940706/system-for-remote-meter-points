from django.contrib import admin

from system_for_remote_meter_points.tasks.models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass