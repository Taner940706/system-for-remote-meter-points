from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from system_for_remote_meter_points.SIM.models import SIM
from system_for_remote_meter_points.modems.forms import CreateModemForm, EditModemForm, DeleteModemForm
from system_for_remote_meter_points.modems.models import Modem
from django.contrib import messages

sim = SIM.objects.all()


@login_required
def list_modem(request):
    initial_logged_user = {
        'user': request.user.username
    }
    is_perm = request.user.has_perm('modems.add_modem')
    modem_list = Modem.objects.all()
    if request.method == 'GET':
        form = CreateModemForm(initial=initial_logged_user)
    else:
        form = CreateModemForm(request.POST, initial=initial_logged_user)
        if form.is_valid():
            modem = form.save(commit=False)
            modem.save()
            messages.success(request, "Modem successfully created!")
        else:
            messages.error(request, form.errors)
        return redirect('list modem')

    context = {
        'modem_list': modem_list,
        'form': form,
        'is_perm': is_perm,
        'is_owner': request.user.username,
        'is_superuser': request.user.is_superuser,
        'sim': sim,
    }
    return render(request, 'modems/modem-list-page.html', context)


@permission_required('modems.change_modem')
def edit_modem(request, pk):
    initial_logged_user = {
        'user': request.user.username
    }
    modem_edit = Modem.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditModemForm(instance=modem_edit, initial=initial_logged_user)
    else:
        form = EditModemForm(request.POST, instance=modem_edit, initial=initial_logged_user)
        if form.is_valid():
            modem = form.save(commit=False)
            modem.save()
            messages.success(request, "Modem successfully updated!")
        else:
            messages.error(request, form.errors)
        return redirect('list modem')

    context = {
        'form': form,
        'modem_edit': modem_edit,
        'sim': sim,
    }
    return render(request, 'modems/modem-edit-page.html', context)


@permission_required('modems.delete_modem')
def delete_modem(request, pk):
    initial_logged_user = {
        'user': request.user.username
    }
    modem_delete = Modem.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteModemForm(instance=modem_delete, initial=initial_logged_user)
    else:
        form = DeleteModemForm(request.POST, instance=modem_delete, initial=initial_logged_user)
        if form.is_valid():
            form.save()
            messages.success(request, "Modem successfully deleted!")
        else:
            messages.error(request, form.errors)
        return redirect('list modem')

    context = {
        'form': form,
        'modem_delete': modem_delete,
    }
    return render(request, 'modems/modem-delete-page.html', context)
