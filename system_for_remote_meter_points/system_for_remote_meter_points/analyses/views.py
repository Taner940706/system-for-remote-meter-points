from django.shortcuts import render

from system_for_remote_meter_points.meter_devices.models import MeterDevice
from system_for_remote_meter_points.meter_points.models import MeterPoint
from system_for_remote_meter_points.tasks.models import Task


# Create your views here.
def type_task_by_count(request):

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
    return render(request, 'analyses/type_task_by_count.html', context)


def result_task_by_count(request):

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

    return render(request, 'analyses/result_task_by_count.html', context)


def count_type_meter_device(request):

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

    return render(request, 'analyses/count_type_meter_device.html', context)


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



