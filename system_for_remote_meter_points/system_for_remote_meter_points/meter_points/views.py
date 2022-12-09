from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect

from system_for_remote_meter_points.meter_points.forms import CreateMeterPointForm, \
	EditMeterPointForm, DeleteMeterPointForm
from system_for_remote_meter_points.meter_points.models import MeterPoint
from system_for_remote_meter_points.tasks.models import Task
from django.contrib import messages


@login_required
def list_meter_point(request):
	initial_logged_user = {
		'user': request.user.username
	}
	is_perm = request.user.has_perm('meter_points.add_meterpoint')
	is_superuser = request.user.is_superuser
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
			messages.success(request, "Meter point successfully created!")
		else:
			messages.error(request, "Meter point doesn't created!")
		return redirect('list meter points')
	context = {
		'meter_point_list': meter_point_list,
		'form': form,
		'is_owner': request.user.username,
		'is_perm': is_perm,
		'is_superuser': is_superuser,

	}
	return render(request, 'meter_points/meter-point-list-page.html', context)


@permission_required('meter_points.change_meterpoint')
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
			messages.success(request, "Meter point successfully updated!")
		else:
			messages.error(request, "Meter point doesn't updated!")
		return redirect('list meter points')

	context = {
		'form': form,
		'meter_point_edit': meter_point_edit,
	}
	return render(request, 'meter_points/meter-point-edit-page.html', context)


@permission_required('meter_points.delete_meterpoint')
def delete_meter_point(request, pk):
	# initial_logged_user = {
	# 	'user': request.user.username
	# }
	meter_point_delete = MeterPoint.objects.filter(pk=pk).get()

	if request.method == 'GET':
		# form = DeleteMeterPointForm(instance=meter_point_delete, initial=initial_logged_user)
		form = DeleteMeterPointForm(instance=meter_point_delete)

	else:
		# form = DeleteMeterPointForm(request.POST, instance=meter_point_delete, initial=initial_logged_user)
		form = DeleteMeterPointForm(request.POST, instance=meter_point_delete)
		# create_task = Task.objects.create(mp_name=form['mp_name'].value(), constant=form['constant'].value(),
		# 								  voltage=form['voltage'].value(),
		# 								  regional_center=form['regional_center'].value(),
		# 								  operation=form['operation'].value(),
		# 								  result_operation=form['result_operation'].value(),
		# 								  comment=form['comment'].value(),
		# 								  modem=form['modem'].value(), meter_device=form['meter_device'].value(),
		# 								  username=form['user'].value())

		create_task = Task.objects.create(mp_name=meter_point_delete.mp_name, constant=meter_point_delete.constant,
										  voltage=meter_point_delete.voltage,
										  regional_center=meter_point_delete.regional_center,
										  operation=meter_point_delete.operation,
										  result_operation=meter_point_delete.result_operation,
										  comment=meter_point_delete.comment,
										  modem=meter_point_delete.modem_id ,meter_device=meter_point_delete.meter_device_id,
										  username=meter_point_delete.user_id)
		if form.is_valid():
			create_task.save()
			form.save()
			messages.success(request, "Meter point successfully deleted!")

		else:
			messages.error(request, "Meter point doesn't deleted!")
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
