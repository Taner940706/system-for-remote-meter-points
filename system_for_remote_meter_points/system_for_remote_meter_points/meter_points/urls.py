from django.urls import path, include

from system_for_remote_meter_points.meter_points.views import edit_meter_point, delete_meter_point, \
    list_meter_point

urlpatterns = (
    path('', list_meter_point, name='list meter points'),
    path('<int:pk>/', include([
        path('edit/', edit_meter_point, name='edit meter points'),
        path('delete/', delete_meter_point, name='delete meter points'),
    ]))
)