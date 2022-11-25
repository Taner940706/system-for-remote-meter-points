from django.shortcuts import render, redirect

from system_for_remote_meter_points.modems.forms import CreateModemForm, EditModemForm, DeleteModemForm
from system_for_remote_meter_points.modems.models import Modem


def list_modem(request):
	modem_list = Modem.objects.all()
	context = {
		'modem_list': modem_list,
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


def edit_modem(request):
	if request.method == 'GET':
		form = EditModemForm()
	else:
		form = EditModemForm(request.POST)
		if form.is_valid():
			modem = form.save(commit=False)
			modem.save()
			return redirect('list modem')

	context = {
		'form': form,
	}
	return render(request, 'modems/modem-edit-page.html', context)


def delete_modem(request):
	if request.method == 'GET':
		form = DeleteModemForm()
	else:
		form = DeleteModemForm(request.POST)
		if form.is_valid():
			modem = form.save(commit=False)
			modem.save()
			return redirect('list modem')

	context = {
		'form': form,
	}
	return render(request, 'modems/modem-delete-page.html', context)
