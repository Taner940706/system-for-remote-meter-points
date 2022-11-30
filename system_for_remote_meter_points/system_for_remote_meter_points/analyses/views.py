from django.shortcuts import render

from system_for_remote_meter_points.meter_devices.models import MeterDevice
from system_for_remote_meter_points.tasks.models import Task


# Create your views here.
def type_task_by_count(request):

    restore_task_type = Task.objects.filter(operation="Restore communication").count()
    add_new_meter_point_task_type = Task.objects.filter(operation="Add new meter points").count()
    replace_meter_device_task_type = Task.objects.filter(operation="Replace meter device").count()
    replace_modem_sim_task_type = Task.objects.filter(operation="Replace modem and/or SIM card").count()
    delete_meter_point_task_type = Task.objects.filter(operation="Delete meter points").count()
    add_new_constant_task_type = Task.objects.filter(operation="Add new constant").count()
    in_comment_task_type = Task.objects.filter(operation="Other").count()

    label = ['Restore communication', 'Add new meter points', 'Replace meter device', 'Replace modem and/or SIM card', 'Delete meter points', 'Add new constant', 'Other']
    data = [restore_task_type, add_new_meter_point_task_type, replace_meter_device_task_type, replace_modem_sim_task_type, delete_meter_point_task_type, add_new_constant_task_type, in_comment_task_type]

    context = {
        'label': label,
        'data': data,
    }
    return render(request, 'analyses/type_task_by_count.html', context)


def result_task_by_count(request):

    successful_task = Task.objects.filter(result_operation="Successful communication").count()
    failed_task = Task.objects.filter(result_operation="No communication").count()
    in_progress_task = Task.objects.filter(result_operation="In progress...").count()

    label = ['Successful communication', 'No communication', 'In progress...']
    data = [successful_task, failed_task, in_progress_task]

    context = {
        'label': label,
        'data': data,
    }

    return render(request, 'analyses/result_task_by_count.html', context)


def count_type_meter_device(request):

    meter_device_iskra = MeterDevice.objects.filter(meter_device_type='ISKRA').count()
    meter_device_amt = MeterDevice.objects.filter(meter_device_type='AMT').count()
    meter_device_microstar = MeterDevice.objects.filter(meter_device_type='Microstar').count()
    meter_device_gama = MeterDevice.objects.filter(meter_device_type='Gama').count()


    label = ['Iskra', 'AMT', 'Microstar', 'Game']
    data = [meter_device_iskra, meter_device_amt, meter_device_microstar, meter_device_gama]

    context = {
        'label': label,
        'data': data,
    }

    return render(request, 'analyses/count_type_meter_device.html', context)




