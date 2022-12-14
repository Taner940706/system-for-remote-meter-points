from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from system_for_remote_meter_points.SIM.forms import CreateSIMForm, EditSIMForm, DeleteSIMForm
from system_for_remote_meter_points.SIM.models import SIM
from django.contrib import messages


# list and list SIM
@login_required
def list_SIM(request):
    initial_logged_user = {
        'user': request.user.username
    }
    # check if has perm for adding
    is_perm = request.user.has_perm('SIM.add_sim')
    sim_list = SIM.objects.all()
    if request.method == 'GET':
        form = CreateSIMForm(initial=initial_logged_user)
    else:
        form = CreateSIMForm(request.POST, initial=initial_logged_user)
        if form.is_valid():
            sim = form.save(commit=False)
            sim.save()
            messages.success(request, "SIM successfully created!")
        else:
            messages.error(request, form.errors)
        return redirect('list SIM')

    context = {
        'sim_list': sim_list,
        'form': form,
        'is_perm': is_perm,

    }
    return render(request, 'SIM/SIM-list-page.html', context)


# edit SIM
@permission_required('SIM.change_sim')
def edit_SIM(request, pk):
    initial_logged_user = {
        'user': request.user.username
    }
    sim_edit = SIM.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditSIMForm(instance=sim_edit, initial=initial_logged_user)
    else:
        form = EditSIMForm(request.POST, instance=sim_edit, initial=initial_logged_user)
        if form.is_valid():
            sim_1 = form.save(commit=False)
            sim_1.save()
            messages.success(request, "SIM successfully updated!")
        else:
            messages.error(request, form.errors)
        return redirect('list SIM')

    context = {
        'form': form,
        'sim_edit': sim_edit,
    }
    return render(request, 'SIM/SIM-edit-page.html', context)


# delete SIM
@permission_required('SIM.delete_sim')
def delete_SIM(request, pk):
    initial_logged_user = {
        'user': request.user.username
    }
    sim_delete = SIM.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteSIMForm(instance=sim_delete, initial=initial_logged_user)
    else:
        form = DeleteSIMForm(request.POST, instance=sim_delete, initial=initial_logged_user)
        if form.is_valid():
            form.save()
            messages.success(request, "SIM successfully deleted!")
        else:
            messages.error(request, form.errors)
        return redirect('list SIM')

    context = {
        'form': form,
        'sim_delete': sim_delete,
    }
    return render(request, 'SIM/SIM-delete-page.html', context)
