from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from system_for_remote_meter_points.tasks.forms import EditTaskForm, DeleteTaskForm
from system_for_remote_meter_points.tasks.models import Task
from django.contrib import messages


@login_required
def list_task(request):
    task_list = Task.objects.all()
    is_superuser = request.user.is_superuser
    # is_perms = request.user.has_perms('tasks.delete_task', 'tasks.change_task')
    context = {
        'task_list': task_list,
        'is_owner': request.user.username,
        'is_superuser': is_superuser,
        # 'is_perms': is_perms,

    }
    return render(request, 'tasks/task-list-page.html', context)


@permission_required('tasks.change_task')
def edit_task(request, pk):
    task = Task.objects.filter(pk=pk).get()
    if request.method == "POST":
        form = EditTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task successfully updated!")
        else:
            messages.error(request, "Task doesn't updated!")
        return redirect('list task')

    else:
        form = EditTaskForm(instance=task)
    context = {
        'form': form,
        'task': task,
    }
    return render(request, 'tasks/task-edit-page.html', context)


@permission_required('tasks.delete_task')
def delete_task(request, pk):
    task = Task.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = DeleteTaskForm(instance=task)
    else:

        form = DeleteTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task successfully deleted!")
        else:
            messages.error(request, "Task doesn't deleted!")
        return redirect('list task')

    context = {
        'form': form,
        'task': task,
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