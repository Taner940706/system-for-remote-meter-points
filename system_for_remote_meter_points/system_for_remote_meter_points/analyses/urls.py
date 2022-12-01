from django.urls import path

from system_for_remote_meter_points.analyses.views import type_task_by_count, result_task_by_count, \
    count_type_meter_device, count_tasks_by_username, count_meter_point_by_time, count_meter_points_by_regional_center

urlpatterns = (
    path('count_type_operation/', type_task_by_count, name='count task operations'),
    path('count_result_operation/', result_task_by_count, name='count task result'),
    path('count_type_meter_device/', count_type_meter_device, name='count meter device type'),
    path('count_tasks_by_username/', count_tasks_by_username, name='count tasks username'),
    path('count_meter_point_by_time/', count_meter_point_by_time, name='count meter point time'),
    path('count_meter_points_by_regional_center/', count_meter_points_by_regional_center, name='count meter point by regional center'),
)