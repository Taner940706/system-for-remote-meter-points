from django.shortcuts import render


def list_modem(request):
	return render(request, 'modems/modem-list-page.html')


def add_modem(request):
	return render(request, 'modems/modem-add-page.html')


def edit_modem(request, pk):
	return render(request, 'modems/modem-edit-page.html')


def delete_modem(request, pk):
	return render(request, 'modems/modem-delete-page.html')
