from django.urls import path

from system_for_remote_meter_points.analyses.views import type_task_by_count, result_task_by_count, \
    count_type_meter_device

urlpatterns = (
    path('count_type_operation/', type_task_by_count, name='count task operations'),
    path('count_result_operation/', result_task_by_count, name='count task result'),
    path('count_type_meter_device/', count_type_meter_device, name='count meter device type'),
)