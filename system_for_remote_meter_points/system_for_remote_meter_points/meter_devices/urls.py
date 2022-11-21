from django.urls import path, include

from system_for_remote_meter_points.meter_devices.views import add_meter_device, edit_meter_device, delete_meter_device, \
    list_meter_device

urlpatterns = (
    path('', list_meter_device, name='list meter device'),
    path('add/', add_meter_device, name='add meter device'),

    path('<int:pk>/', include([
        path('edit/', edit_meter_device, name='edit meter device'),
        path('delete/', delete_meter_device, name='delete meter device'),
    ]))
)