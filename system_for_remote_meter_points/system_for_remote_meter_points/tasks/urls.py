from django.urls import path, include

from system_for_remote_meter_points.tasks.views import edit_task, delete_task, list_task, details_task

urlpatterns = (
    path('', list_task, name='list task'),
    path('<int:pk>/', include([
        path('edit/', edit_task, name='edit task'),
        path('delete/', delete_task, name='delete task'),
        path('details/', details_task, name='details task'),
    ]))
)
