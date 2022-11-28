from django.shortcuts import render, redirect

from system_for_remote_meter_points.meter_points.forms import CreateMeterPointForm, \
	EditMeterPointForm, DeleteMeterPointForm
from system_for_remote_meter_points.meter_points.models import MeterPoint
from system_for_remote_meter_points.tasks.models import Task


def list_meter_point(request):
	meter_point_list = MeterPoint.objects.all()
	if request.method == 'GET':
		form = CreateMeterPointForm()
	else:
		form = CreateMeterPointForm(request.POST)
		create_task = Task.objects.create(mp_name=form['mp_name'].value(), constant=form['constant'].value(),
										   voltage=form['voltage'].value(),
										  regional_center=form['regional_center'].value(), operation=form['operation'].value(), result_operation=form['result_operation'].value(), comment=form['comment'].value(),
										  modem=form['modem'].value(), meter_device=form['meter_device'].value())
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
	meter_point_edit = MeterPoint.objects.filter(pk=pk).get()
	if request.method == 'GET':
		form = EditMeterPointForm(instance=meter_point_edit)
	else:
		form = EditMeterPointForm(request.POST, instance=meter_point_edit)
		create_task = Task.objects.create(mp_name=form['mp_name'].value(), constant=form['constant'].value(),
										  voltage=form['voltage'].value(),
										  regional_center=form['regional_center'].value(),
										  operation=form['operation'].value(),
										  result_operation=form['result_operation'].value(),
										  comment=form['comment'].value(),
										  modem=form['modem'].value(), meter_device=form['meter_device'].value())
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
	meter_point_delete = MeterPoint.objects.filter(pk=pk).get()
	if request.method == 'GET':
		form = DeleteMeterPointForm(instance=meter_point_delete)
	else:
		form = DeleteMeterPointForm(request.POST, instance=meter_point_delete)
		create_task = Task.objects.create(mp_name=form['mp_name'].value(), constant=form['constant'].value(),
										  voltage=form['voltage'].value(),
										  regional_center=form['regional_center'].value(),
										  operation=form['operation'].value(),
										  result_operation=form['result_operation'].value(),
										  comment=form['comment'].value(),
										  modem=form['modem'].value(), meter_device=form['meter_device'].value())
		if form.is_valid():
			form.save()
			create_task.save()
			return redirect('list meter points')

	context = {
		'form': form,
		'meter_point_delete': meter_point_delete,
	}
	return render(request, 'meter_points/meter-point-delete-page.html', context)
