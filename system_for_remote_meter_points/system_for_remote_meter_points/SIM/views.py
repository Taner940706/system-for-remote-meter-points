from django.shortcuts import render, redirect
from system_for_remote_meter_points.SIM.forms import CreateSIMForm, EditSIMForm, DeleteSIMForm
from system_for_remote_meter_points.SIM.models import SIM



def list_SIM(request):
	sim_list = SIM.objects.all()
	if request.method == 'GET':
		form = CreateSIMForm()
	else:
		form = CreateSIMForm(request.POST)
		if form.is_valid():
			sim = form.save(commit=False)
			sim.save()
			return redirect('list SIM')
	context = {
		'sim_list': sim_list,
		'form': form,

	}
	return render(request, 'SIM/SIM-list-page.html', context)


def edit_SIM(request, pk):
	sim_list_1 = SIM.objects.filter(pk=pk).get()
	if request.method == 'GET':
		form_1 = EditSIMForm(instance=sim_list_1)
	else:
		form_1 = EditSIMForm(request.POST, instance=sim_list_1)
		if form_1.is_valid():
			sim_1 = form_1.save(commit=False)
			sim_1.save()
			return redirect('list SIM')

	context = {
		'form_1': form_1,
		'sim_list_1': sim_list_1,
	}
	return render(request, 'SIM/SIM-edit-page.html', context)


def delete_SIM(request, pk):
	sim_list_2 = SIM.objects.filter(pk=pk).get()
	if request.method == 'GET':
		form = DeleteSIMForm(instance=sim_list_2)
	else:
		form = DeleteSIMForm(request.POST, instance=sim_list_2)
		if form.is_valid():
			form.save()
			return redirect('list SIM')

	context = {
		'form': form,
		'sim_list_2': sim_list_2,
	}
	return render(request, 'SIM/SIM-delete-page.html', context)
