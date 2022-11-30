from django.shortcuts import render

from system_for_remote_meter_points.meter_devices.models import MeterDevice
from system_for_remote_meter_points.tasks.models import Task


# Create your views here.
def type_task_by_count(request):

    # restore_task_type = Task.objects.filter(operation="Restore communication").count()
    # add_new_meter_point_task_type = Task.objects.filter(operation="Add new meter points").count()
    # replace_meter_device_task_type = Task.objects.filter(operation="Replace meter device").count()
    # replace_modem_sim_task_type = Task.objects.filter(operation="Replace modem and/or SIM card").count()
    # delete_meter_point_task_type = Task.objects.filter(operation="Delete meter points").count()
    # add_new_constant_task_type = Task.objects.filter(operation="Add new constant").count()
    # in_comment_task_type = Task.objects.filter(operation="Other").count()

    # label = ['Restore communication', 'Add new meter points', 'Replace meter device', 'Replace modem and/or SIM card', 'Delete meter points', 'Add new constant', 'Other']
    # data = [restore_task_type, add_new_meter_point_task_type, replace_meter_device_task_type, replace_modem_sim_task_type, delete_meter_point_task_type, add_new_constant_task_type, in_comment_task_type]

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




