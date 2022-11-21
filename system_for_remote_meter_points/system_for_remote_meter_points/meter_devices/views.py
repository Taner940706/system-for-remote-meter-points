from django.shortcuts import render


def list_meter_device(request):
	return render(request, 'meter_devices/meter-device-list-page.html')


def add_meter_device(request):
	return render(request, 'meter_devices/meter-device-add-page.html')


def edit_meter_device(request, pk):
	return render(request, 'meter_devices/meter-device-edit-page.html')


def delete_meter_device(request, pk):
	return render(request, 'meter_devices/meter-device-delete-page.html')