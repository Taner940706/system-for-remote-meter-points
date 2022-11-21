from django.shortcuts import render


def list_task(request):
	return render(request, 'tasks/task-list-page.html')


def edit_task(request, pk):
	return render(request, 'tasks/task-edit-page.html')


def delete_task(request, pk):
	return render(request, 'tasks/task-delete-page.html')
