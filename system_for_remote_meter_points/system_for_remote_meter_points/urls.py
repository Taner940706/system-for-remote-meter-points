from django.conf import settings
from django.conf.urls.static import static
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
    path('api/', include('system_for_remote_meter_points.api.urls')),
]
# Media folder
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'system_for_remote_meter_points.accounts.views.handler_404'
handler500 = 'system_for_remote_meter_points.accounts.views.handler_500'
