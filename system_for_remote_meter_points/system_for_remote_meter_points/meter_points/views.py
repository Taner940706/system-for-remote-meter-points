from django.shortcuts import render, redirect

from system_for_remote_meter_points.meter_points.forms import CreateMeterPointForm, \
	EditMeterPointForm, DeleteMeterPointForm
from system_for_remote_meter_points.meter_points.models import MeterPoint
from system_for_remote_meter_points.tasks.models import Task


def list_meter_point(request):
	initial_logged_user = {
		'user': request.user.username
	}
	meter_point_list = MeterPoint.objects.all()
	if request.method == 'GET':
		form = CreateMeterPointForm(initial=initial_logged_user)

	else:
		form = CreateMeterPointForm(request.POST, initial=initial_logged_user)
		create_task = Task.objects.create(mp_name=form['mp_name'].value(), constant=form['constant'].value(),
										  voltage=form['voltage'].value(),
										  regional_center=form['regional_center'].value(),
										  operation=form['operation'].value(),
										  result_operation=form['result_operation'].value(),
										  comment=form['comment'].value(),
										  modem=form['modem'].value(), meter_device=form['meter_device'].value(),
										  username=form['user'].value())
		if form.is_valid():
			meter_point = form.save(commit=False)

			meter_point.save()
			create_task.save()
			return redirect('list meter points')
	context = {
		'meter_point_list': meter_point_list,
		'form': form,

	}
	return render(request, 'meter_points/meter-point-list-page.html', context)



def edit_meter_point(request, pk):
	initial_logged_user = {
		'user': request.user.username
	}
	meter_point_edit = MeterPoint.objects.filter(pk=pk).get()
	if request.method == 'GET':
		form = EditMeterPointForm(instance=meter_point_edit, initial=initial_logged_user)
	else:
		form = EditMeterPointForm(request.POST, instance=meter_point_edit, initial=initial_logged_user)
		create_task = Task.objects.create(mp_name=form['mp_name'].value(), constant=form['constant'].value(),
										  voltage=form['voltage'].value(),
										  regional_center=form['regional_center'].value(),
										  operation=form['operation'].value(),
										  result_operation=form['result_operation'].value(),
										  comment=form['comment'].value(),
										  modem=form['modem'].value(), meter_device=form['meter_device'].value(), username=form['user'].value())
		if form.is_valid():
			meter_point = form.save(commit=False)
			meter_point.save()
			create_task.save()
			return redirect('list meter points')

	context = {
		'form': form,
		'meter_point_edit': meter_point_edit,
	}
	return render(request, 'meter_points/meter-point-edit-page.html', context)


def delete_meter_point(request, pk):
	initial_logged_user = {
		'user': request.user.username
	}
	meter_point_delete = MeterPoint.objects.filter(pk=pk).get()
	if request.method == 'GET':
		form = DeleteMeterPointForm(instance=meter_point_delete, initial=initial_logged_user)
	else:
		form = DeleteMeterPointForm(request.POST, instance=meter_point_delete, initial=initial_logged_user)
		create_task = Task.objects.create(mp_name=form['mp_name'].value(), constant=form['constant'].value(),
										  voltage=form['voltage'].value(),
										  regional_center=form['regional_center'].value(),
										  operation=form['operation'].value(),
										  result_operation=form['result_operation'].value(),
										  comment=form['comment'].value(),
										  modem=form['modem'].value(), meter_device=form['meter_device'].value(),
										  username=form['user'].value())
		if form.is_valid():
			form.save()
			create_task.save()
			return redirect('list meter points')

	context = {
		'form': form,
		'meter_point_delete': meter_point_delete,
	}
	return render(request, 'meter_points/meter-point-delete-page.html', context)


def details_meter_point(request, pk):
	meter_point_details = MeterPoint.objects \
		.filter(pk=pk) \
		.get()

	context = {
		'meter_point_details': meter_point_details,
	}

	return render(request, 'meter_points/meter-point-details-page.html', context)


def details_task(request, pk):
	task_details = Task.objects \
		.filter(pk=pk) \
		.get()

	context = {
		'task_details': task_details,
	}

	return render(request, 'tasks/task-details-page.html', context)