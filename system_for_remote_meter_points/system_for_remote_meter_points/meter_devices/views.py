from django.shortcuts import render, redirect

from system_for_remote_meter_points.meter_devices.forms import CreateMeterDeviceForm, \
	EditMeterDeviceForm, DeleteMeterDeviceForm
from system_for_remote_meter_points.meter_devices.models import MeterDevice


def list_meter_device(request):
	meter_device_list = MeterDevice.objects.all()
	context = {
		'meter_device_list': meter_device_list,
	}
	return render(request, 'meter_devices/meter-device-list-page.html', context)


def add_meter_device(request):
	if request.method == 'GET':
		form = CreateMeterDeviceForm()
	else:
		form = CreateMeterDeviceForm(request.POST)
		if form.is_valid():
			modem = form.save(commit=False)
			modem.save()
			return redirect('list meter device')

	context = {
		'form': form,
	}
	return render(request, 'meter_devices/meter-device-add-page.html', context)


def edit_meter_device(request):
	if request.method == 'GET':
		form = EditMeterDeviceForm()
	else:
		form = EditMeterDeviceForm(request.POST)
		if form.is_valid():
			modem = form.save(commit=False)
			modem.save()
			return redirect('list meter device')

	context = {
		'form': form,
	}
	return render(request, 'meter_devices/meter-device-edit-page.html', context)


def delete_meter_device(request):
	if request.method == 'GET':
		form = DeleteMeterDeviceForm()
	else:
		form = DeleteMeterDeviceForm(request.POST)
		if form.is_valid():
			modem = form.save(commit=False)
			modem.save()
			return redirect('list meter device')

	context = {
		'form': form,
	}
	return render(request, 'meter_devices/meter-device-delete-page.html', context)
