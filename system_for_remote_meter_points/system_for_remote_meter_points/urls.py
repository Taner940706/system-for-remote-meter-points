
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('system_for_remote_meter_points.accounts.urls')),
    path('analyses/', include('system_for_remote_meter_points.analyses.urls')),
    path('meter-devices/', include('system_for_remote_meter_points.meter_devices.urls')),
    path('meter-points/', include('system_for_remote_meter_points.meter_points.urls')),
    path('modems/', include('system_for_remote_meter_points.modems.urls')),
    path('SIM/', include('system_for_remote_meter_points.SIM.urls')),
    path('tasks/', include('system_for_remote_meter_points.tasks.urls')),
]

handler404 = 'system_for_remote_meter_points.accounts.views.handler_404'