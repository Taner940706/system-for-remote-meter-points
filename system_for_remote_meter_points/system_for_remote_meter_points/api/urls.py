from django.urls import path, include

from system_for_remote_meter_points.api.views import UserListApiView, UserCreateApiView, UserUpdateApiView, \
    UserDeleteApiView, SIMListApiView, SIMCreateApiView, SIMDeleteApiView, SIMUpdateApiView, ModemListApiView, \
    ModemCreateApiView, ModemUpdateApiView, ModemDeleteApiView, MeterDeviceListApiView, MeterDeviceCreateApiView, \
    MeterDeviceUpdateApiView, MeterDeviceDeleteApiView, TaskListApiView, TaskCreateApiView, TaskUpdateApiView, \
    TaskDeleteApiView, MeterPointListApiView, MeterPointCreateApiView, MeterPointUpdateApiView, MeterPointDeleteApiView

urlpatterns = [
    path('users/', UserListApiView.as_view(), name='list users api'),
    path('users/create/', UserCreateApiView.as_view(), name='create user api'),
    path('users/<int:pk>/', include([
        path('edit/', UserUpdateApiView.as_view(), name='update user api'),
        path('delete/', UserDeleteApiView.as_view(), name='delete user api'),
    ])),

    path('sims/', SIMListApiView.as_view(), name='list sims api'),
    path('sims/create/', SIMCreateApiView.as_view(), name='create sim api'),
    path('sims/<int:pk>/', include([
        path('edit/', SIMUpdateApiView.as_view(), name='edit sim api'),
        path('delete/', SIMDeleteApiView.as_view(), name='delete sim api',)
    ])),

    path('modems/', ModemListApiView.as_view(), name='list modems api'),
    path('modems/create/', ModemCreateApiView.as_view(), name='create modem api'),
    path('modems/<int:pk>/', include([
        path('edit/', ModemUpdateApiView.as_view(), name='edit modem api'),
        path('delete/', ModemDeleteApiView.as_view(), name='delete modem api'),
    ])),

    path('meter-devices/', MeterDeviceListApiView.as_view(), name='list meter devices api'),
    path('meter-devices/create/', MeterDeviceCreateApiView.as_view(), name='create meter device api'),
    path('meter-devices/<int:pk>/', include([
        path('edit/', MeterDeviceUpdateApiView.as_view(), name='edit meter device api'),
        path('delete/', MeterDeviceDeleteApiView.as_view(), name='delete meter device api'),
    ])),

    path('tasks/', TaskListApiView.as_view(), name='list tasks api'),
    path('tasks/create/', TaskCreateApiView.as_view(), name='create task api'),
    path('tasks/<int:pk>/', include([
        path('edit/', TaskUpdateApiView.as_view(), name='edit task api'),
        path('delete/', TaskDeleteApiView.as_view(), name='delete task api'),
    ])),

    path('meter-points/', MeterPointListApiView.as_view(), name='list meter points api'),
    path('meter-points/create/', MeterPointCreateApiView.as_view(), name='create meter point api'),
    path('meter-points/<int:pk>/', include([
        path('edit/', MeterPointUpdateApiView.as_view(), name='edit meter point api'),
        path('delete/', MeterPointDeleteApiView.as_view(), name='delete meter point api'),
    ]))

]