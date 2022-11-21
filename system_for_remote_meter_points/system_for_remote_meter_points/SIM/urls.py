from django.urls import path, include

from system_for_remote_meter_points.SIM.views import add_SIM, edit_SIM, delete_SIM, list_SIM

urlpatterns = (
    path('', list_SIM, name='list SIM'),
    path('add/', add_SIM, name='add SIM'),
    path('<int:pk>/', include([
        path('edit/', edit_SIM, name='edit SIM'),
        path('delete/', delete_SIM, name='delete SIM'),
    ]))
)
