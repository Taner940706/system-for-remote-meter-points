from django.urls import path, include

from system_for_remote_meter_points.modems.views import edit_modem, delete_modem, list_modem

urlpatterns = (
    path('', list_modem, name='list modem'),
    path('<int:pk>/', include([
        path('edit/', edit_modem, name='edit modem'),
        path('delete/', delete_modem, name='delete modem'),
    ]))
)