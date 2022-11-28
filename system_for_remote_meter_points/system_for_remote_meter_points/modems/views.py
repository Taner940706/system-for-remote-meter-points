from django.shortcuts import render, redirect

from system_for_remote_meter_points.modems.forms import CreateModemForm, EditModemForm, DeleteModemForm
from system_for_remote_meter_points.modems.models import Modem


def list_modem(request):
	modem_list = Modem.objects.all()
	if request.method == 'GET':
		form = CreateModemForm()
	else:
		form = CreateModemForm(request.POST)
		if form.is_valid():
			modem = form.save(commit=False)
			modem.save()
			return redirect('list modem')
	context = {
		'modem_list': modem_list,
		'form': form,
	}
	return render(request, 'modems/modem-list-page.html', context)


def add_modem(request):
	if request.method == 'GET':
		form = CreateModemForm()
	else:
		form = CreateModemForm(request.POST)
		if form.is_valid():
			modem = form.save(commit=False)
			modem.save()
			return redirect('list modem')

	context = {
		'form': form,
	}
	return render(request, 'modems/modem-add-page.html', context)


def edit_modem(request, pk):
	modem_edit = Modem.objects.filter(pk=pk).get()
	if request.method == 'GET':
		form = EditModemForm(instance=modem_edit)
	else:
		form = EditModemForm(request.POST, instance=modem_edit)
		if form.is_valid():
			modem = form.save(commit=False)
			modem.save()
			return redirect('list modem')

	context = {
		'form': form,
		'modem_edit': modem_edit,
	}
	return render(request, 'modems/modem-edit-page.html', context)


def delete_modem(request, pk):
	modem_delete = Modem.objects.filter(pk=pk).get()
	if request.method == 'GET':
		form = DeleteModemForm(instance=modem_delete)
	else:
		form = DeleteModemForm(request.POST, instance=modem_delete)
		if form.is_valid():
			form.save()
			return redirect('list modem')

	context = {
		'form': form,
		'modem_delete': modem_delete,
	}
	return render(request, 'modems/modem-delete-page.html', context)
