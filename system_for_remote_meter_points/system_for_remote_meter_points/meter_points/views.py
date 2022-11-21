from django.shortcuts import render


def list_meter_point(request):
	return render(request, 'meter_points/meter-point-list-page.html')


def add_meter_point(request):
	return render(request, 'meter_points/meter-point-add-page.html')


def edit_meter_point(request, pk):
	return render(request, 'meter_points/meter-point-edit-page.html')


def delete_meter_point(request, pk):
	return render(request, 'meter_points/meter-point-delete-page.html')
