from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect

from system_for_remote_meter_points.meter_devices.models import MeterDevice
from system_for_remote_meter_points.modems.models import Modem
from system_for_remote_meter_points.tasks.forms import EditTaskForm, DeleteTaskForm
from system_for_remote_meter_points.tasks.models import Task
from django.contrib import messages


@login_required
def list_task(request):
    task_list = Task.objects.all()
    context = {
        'task_list': task_list,
        'is_owner': request.user.username,
        'is_superuser': request.user.is_superuser,

    }
    return render(request, 'tasks/task-list-page.html', context)


@permission_required('tasks.change_task')
def edit_task(request, pk):
    initial_logged_user = {
        'user': request.user.username
    }
    modem = Modem.objects.all()
    meter_device = MeterDevice.objects.all()
    task_edit = Task.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditTaskForm(instance=task_edit, initial=initial_logged_user)
    else:
        form = EditTaskForm(request.POST, instance=task_edit, initial=initial_logged_user)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            messages.success(request, "Task successfully updated!")
        else:
            messages.error(request, form.errors)
        return redirect('list task')

    context = {
        'form': form,
        'task_edit': task_edit,
        'modem': modem,
        'meter_device': meter_device,
    }
    return render(request, 'tasks/task-edit-page.html', context)


@permission_required('tasks.delete_task')
def delete_task(request, pk):
    task_delete = Task.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = DeleteTaskForm(instance=task_delete)
    else:

        form = DeleteTaskForm(request.POST, instance=task_delete)
        if form.is_valid():
            form.save()
            messages.success(request, "Task successfully deleted!")
        else:
            messages.error(request, form.errors)
        return redirect('list task')

    context = {
        'form': form,
        'task_delete': task_delete,
    }
    return render(request, 'tasks/task-delete-page.html', context)


def details_task(request, pk):
    task_details = Task.objects \
        .filter(pk=pk) \
        .get()

    context = {
        'task_details': task_details,
    }

    return render(request, 'tasks/task-details-page.html', context)
