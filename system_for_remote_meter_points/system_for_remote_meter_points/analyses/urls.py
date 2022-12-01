from django.urls import path

from system_for_remote_meter_points.analyses.views import count_task_operations, count_result_tasks, \
    count_meter_device_types, count_tasks_by_username, count_meter_point_by_time, count_meter_points_by_regional_center

urlpatterns = (
    path('count_type_operation/', count_task_operations, name='count task operations'),
    path('count_result_tasks/', count_result_tasks, name='count task results'),
    path('count_meter_device_types/', count_meter_device_types, name='count meter device types'),
    path('count_tasks_by_username/', count_tasks_by_username, name='count tasks by username'),
    path('count_meter_point_by_time/', count_meter_point_by_time, name='count meter point by time'),
    path('count_meter_points_by_regional_center/', count_meter_points_by_regional_center, name='count meter point by regional center'),
)