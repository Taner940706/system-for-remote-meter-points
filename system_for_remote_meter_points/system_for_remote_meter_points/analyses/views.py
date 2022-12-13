from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from system_for_remote_meter_points.meter_devices.models import MeterDevice
from system_for_remote_meter_points.meter_points.models import MeterPoint
from system_for_remote_meter_points.tasks.models import Task


# diagram for count tasks by operation type
@login_required
def count_task_operations(request):
    label = []
    data = []

    tasks = Task.objects.all()
    for task in tasks:
        if task.operation not in label:
            label.append(task.operation)

    for lab in label:
        data.append(Task.objects.filter(operation=lab).count())

    context = {
        'label': label,
        'data': data,
    }
    return render(request, 'analyses/count_type_operation.html', context)


# diagram for count tasks by result operation type
@login_required
def count_result_tasks(request):
    label = []
    data = []

    tasks = Task.objects.all()
    for task in tasks:
        if task.result_operation not in label:
            label.append(task.result_operation)

    for lab in label:
        data.append(Task.objects.filter(result_operation=lab).count())

    context = {
        'label': label,
        'data': data,
    }

    return render(request, 'analyses/count_result_tasks.html', context)


# diagram for count meter device by type
@login_required
def count_meter_device_types(request):
    label = []
    data = []

    meter_devices = MeterDevice.objects.all()
    for meter_device in meter_devices:
        if meter_device.meter_device_type not in label:
            label.append(meter_device.meter_device_type)

    for lab in label:
        data.append(MeterDevice.objects.filter(meter_device_type=lab).count())

    context = {
        'label': label,
        'data': data,
    }

    return render(request, 'analyses/count_meter_device_types.html', context)


# diagram for count tasks by username
@login_required
def count_tasks_by_username(request):
    label = []
    data = []

    tasks = Task.objects.all()
    for task in tasks:
        if task.username not in label:
            label.append(task.username)

    for lab in label:
        data.append(Task.objects.filter(username=lab).count())

    context = {
        'label': label,
        'data': data,
    }

    return render(request, 'analyses/count_tasks_by_username.html', context)


# diagram for count meter points in time
@login_required
def count_meter_point_by_time(request):
    label = []
    data = []

    tasks = Task.objects.all().order_by('created_date')
    for task in tasks:
        if task.created_date not in label:
            label.append(task.created_date)

    for lab in label:
        data.append(Task.objects.filter(created_date=lab).count())

    context = {
        'label': label,
        'data': data,
    }

    return render(request, 'analyses/count_meter_point_by_time.html', context)


# diagram for count meter points by regional center
@login_required
def count_meter_points_by_regional_center(request):
    label = []
    data = []

    meter_points = MeterPoint.objects.all()
    for meter_point in meter_points:
        if meter_point.regional_center not in label:
            label.append(meter_point.regional_center)

    for lab in label:
        data.append(MeterPoint.objects.filter(regional_center=lab).count())

    context = {
        'label': label,
        'data': data,
    }

    return render(request, 'analyses/count_meter_points_by_regional_center.html', context)


# dashboard cards and alert messages
@login_required
def dashboard(request):
    count_success_tasks = Task.objects.filter(result_operation="Successful communication").filter(
        username=request.user.username).count()
    count_failed_tasks = Task.objects.filter(result_operation="No communication").filter(
        username=request.user.username).count()
    count_in_progress_tasks = Task.objects.filter(result_operation="In progress...").filter(
        username=request.user.username).count()
    count_all_meter_points = MeterPoint.objects.all().count()
    count_all_tasks = Task.objects.all().count()
    count_all_tasks_today = Task.objects.filter(created_date=datetime.now().date()).filter(
        username=request.user.username).count()

    context = {
        'count_success_tasks': count_success_tasks,
        'count_failed_tasks': count_failed_tasks,
        'count_in_progress_tasks': count_in_progress_tasks,
        'count_all_meter_points': count_all_meter_points,
        'count_all_tasks': count_all_tasks,
        'count_all_tasks_today': count_all_tasks_today,
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
    }

    return render(request, 'analyses/../../templates/accounts/dashboard.html', context)
