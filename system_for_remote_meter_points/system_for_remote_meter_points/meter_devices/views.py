from django.shortcuts import render, redirect
from system_for_remote_meter_points.meter_devices.forms import CreateMeterDeviceForm, \
	EditMeterDeviceForm, DeleteMeterDeviceForm
from system_for_remote_meter_points.meter_devices.models import MeterDevice



def list_meter_device(request):
	initial_logged_user = {
		'user': request.user.username
	}
	meter_device_list = MeterDevice.objects.all()

	if request.method == 'GET':
		form = CreateMeterDeviceForm(initial=initial_logged_user)
	else:
		form = CreateMeterDeviceForm(request.POST, initial=initial_logged_user)
		if form.is_valid():
			modem = form.save(commit=False)
			modem.save()
			return redirect('list meter device')
	context = {
		'meter_device_list': meter_device_list,
		'form': form,

	}
	return render(request, 'meter_devices/meter-device-list-page.html', context)


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
			return redirect('list meter device')

	context = {
		'form': form,
		'meter_device_edit': meter_device_edit,
	}
	return render(request, 'meter_devices/meter-device-edit-page.html', context)


def delete_meter_device(request, pk):
	initial_logged_user = {
		'user': request.user.username
	}
	meter_device_delete = MeterDevice.objects.filter(pk=pk).get()
	if request.method == 'GET':
		form = DeleteMeterDeviceForm(instance=meter_device_delete, initial=initial_logged_user)
	else:
		form = DeleteMeterDeviceForm(request.POST, instance=meter_device_delete, initial=initial_logged_user)
		if form.is_valid():
			form.save()
			return redirect('list meter device')

	context = {
		'form': form,
		'meter_device_delete': meter_device_delete,
	}
	return render(request, 'meter_devices/meter-device-delete-page.html', context)
