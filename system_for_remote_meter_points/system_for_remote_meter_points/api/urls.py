from django.urls import path, include

from system_for_remote_meter_points.api.views import UserListApiView, UserCreateApiView, UserUpdateApiView, \
    UserDeleteApiView, SIMListApiView, SIMCreateApiView, SIMDeleteApiView, SIMUpdateApiView, ModemListApiView, \
    ModemCreateApiView, ModemUpdateApiView, ModemDeleteApiView

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

]