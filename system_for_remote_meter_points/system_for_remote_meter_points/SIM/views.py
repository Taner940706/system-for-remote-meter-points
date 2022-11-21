from django.shortcuts import render


def list_SIM(request):
	return render(request, 'SIM/SIM-list-page.html')


def add_SIM(request):
	return render(request, 'SIM/SIM-add-page.html')


def edit_SIM(request, pk):
	return render(request, 'SIM/SIM-edit-page.html')


def delete_SIM(request, pk):
	return render(request, 'SIM/SIM-delete-page.html')
