from django.shortcuts import render, redirect

from system_for_remote_meter_points.meter_points.forms import CreateMeterPointForm, \
	EditMeterPointForm, DeleteMeterPointForm
from system_for_remote_meter_points.meter_points.models import MeterPoint
from system_for_remote_meter_points.tasks.forms import TaskBaseForm


def list_meter_point(request):
	meter_point_list = MeterPoint.objects.all()
	context = {
		'meter_point_list': meter_point_list,
	}
	return render(request, 'meter_points/meter-point-list-page.html', context)


def add_meter_point(request):
	if request.method == 'GET':
		form = CreateMeterPointForm()
	else:
		form = CreateMeterPointForm(request.POST)
		form_task = TaskBaseForm(request.POST)
		if form.is_valid():
			meter_point = form.save(commit=False)
			task = form_task.save(commit=False)
			task.save()
			meter_point.save()
			return redirect('list meter points')

	context = {
		'form': form,
	}
	return render(request, 'meter_points/meter-point-add-page.html', context)


def edit_meter_point(request):
	if request.method == 'GET':
		form = EditMeterPointForm()
	else:
		form = EditMeterPointForm(request.POST)
		form_task = TaskBaseForm(request.POST)
		if form.is_valid():
			meter_point = form.save(commit=False)
			task = form_task.save(commit=False)
			task.save()
			meter_point.save()
			return redirect('list meter points')

	context = {
		'form': form,
	}
	return render(request, 'meter_points/meter-point-edit-page.html', context)


def delete_meter_point(request, pk):
	if request.method == 'GET':
		form = DeleteMeterPointForm()
	else:
		form = DeleteMeterPointForm(request.POST)
		form_task = TaskBaseForm(request.POST)
		if form.is_valid():
			meter_point = form.save(commit=False)
			task = form_task.save(commit=False)
			task.save()
			meter_point.save()
			return redirect('list meter points')

	context = {
		'form': form,
	}
	return render(request, 'meter_points/meter-point-delete-page.html', context)
