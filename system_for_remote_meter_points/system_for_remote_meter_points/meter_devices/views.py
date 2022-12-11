from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from system_for_remote_meter_points.meter_devices.forms import CreateMeterDeviceForm, \
	EditMeterDeviceForm, DeleteMeterDeviceForm
from system_for_remote_meter_points.meter_devices.models import MeterDevice
from django.contrib import messages


@login_required
def list_meter_device(request):
	initial_logged_user = {
		'user': request.user.username
	}
	# tst = (request.user.get_all_permissions())
	is_superuser = request.user.is_superuser
	is_perm = request.user.has_perm('meter_devices.add_meterdevice')
	meter_device_list = MeterDevice.objects.all()

	if request.method == 'GET':
		form = CreateMeterDeviceForm(initial=initial_logged_user)
	else:
		form = CreateMeterDeviceForm(request.POST, initial=initial_logged_user)
		if form.is_valid():
			modem = form.save(commit=False)
			modem.save()
			messages.success(request, "Meter device successfully created!")
		else:
			messages.error(request, form.errors)
		return redirect('list meter device')

	context = {
		'meter_device_list': meter_device_list,
		'form': form,
		'is_owner': request.user.username,
		'is_perm': is_perm,
		'is_superuser': is_superuser,

	}
	return render(request, 'meter_devices/meter-device-list-page.html', context)


@permission_required('meter_devices.change_meterdevice')
def edit_meter_device(request, pk):
	initial_logged_user = {
		'user': request.user.username
	}
	meter_device_edit = MeterDevice.objects.filter(pk=pk).get()
	if request.method == 'GET':
		form = EditMeterDeviceForm(instance=meter_device_edit, initial=initial_logged_user)
	else:
		form = EditMeterDeviceForm(request.POST, instance=meter_device_edit, initial=initial_logged_user)
		if form.is_valid():
			modem = form.save(commit=False)
			modem.save()
			messages.success(request, "Meter device successfully updated!")
		else:
			messages.error(request, form.errors)
		return redirect('list meter device')

	context = {
		'form': form,
		'meter_device_edit': meter_device_edit,
	}
	return render(request, 'meter_devices/meter-device-edit-page.html', context)


@permission_required('meter_devices.delete_meterdevice')
def delete_meter_device(request, pk):
	# initial_logged_user = {
	# 	'user': request.user.username
	# }
	meter_device_delete = MeterDevice.objects.filter(pk=pk).get()
	if request.method == 'GET':
		form = DeleteMeterDeviceForm(instance=meter_device_delete)
	else:
		form = DeleteMeterDeviceForm(request.POST, instance=meter_device_delete)
		if form.is_valid():
			form.save()
			messages.success(request, "Meter device successfully deleted!")
		else:
			messages.error(request, form.errors)
		return redirect('list meter device')

	context = {
		'form': form,
		'meter_device_delete': meter_device_delete,
	}
	return render(request, 'meter_devices/meter-device-delete-page.html', context)
