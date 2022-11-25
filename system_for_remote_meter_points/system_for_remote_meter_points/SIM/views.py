from django.shortcuts import render, redirect

from system_for_remote_meter_points.SIM.forms import  CreateSIMForm, EditSIMForm, DeleteSIMForm
from system_for_remote_meter_points.SIM.models import SIM


def list_SIM(request):
	sim_list = SIM.objects.all()
	context = {
		'sim_list': sim_list,
	}
	return render(request, 'SIM/SIM-list-page.html', context)


def add_SIM(request):
	if request.method == 'GET':
		form = CreateSIMForm()
	else:
		form = CreateSIMForm(request.POST)
		if form.is_valid():
			sim = form.save(commit=False)
			sim.save()
			return redirect('list SIM')

	context = {
		'form': form,
	}
	return render(request, 'SIM/SIM-add-page.html', context)


def edit_SIM(request):

	if request.method == 'GET':
		form = EditSIMForm()
	else:
		form = EditSIMForm(request.POST)
		if form.is_valid():
			sim = form.save(commit=False)
			sim.save()
			return redirect('list SIM')

	context = {
		'form': form,
	}
	return render(request, 'SIM/SIM-edit-page.html', context)


def delete_SIM(request):

	if request.method == 'GET':
		form = DeleteSIMForm()
	else:
		form = DeleteSIMForm(request.POST)
		if form.is_valid():
			sim = form.save(commit=False)
			sim.save()
			return redirect('list SIM')

	context = {
		'form': form,
	}
	return render(request, 'SIM/SIM-delete-page.html', context)
