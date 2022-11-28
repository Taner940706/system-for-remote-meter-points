from django.shortcuts import render, redirect

from system_for_remote_meter_points.tasks.forms import EditTaskForm, DeleteTaskForm
from system_for_remote_meter_points.tasks.models import Task


def list_task(request):
	task_list = Task.objects.all()
	context = {
		'task_list': task_list,
	}
	return render(request, 'tasks/task-list-page.html', context)


def edit_task(request, pk):
	task = Task.objects.filter(pk=pk).get()
	if request.method == "POST":
		form = EditTaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('list task')
	else:
		form = EditTaskForm(instance=task)
	context = {
		'form': form,
		'task': task,
	}
	return render(request, 'tasks/task-edit-page.html', context)


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
			return redirect('list task')

	context = {
		'form': form,
		'task': task,
	}
	return render(request, 'tasks/task-delete-page.html', context)
