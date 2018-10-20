from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Inventory, Computer
from .forms import computerForm, inventoryForm

def index(request):
    all_inventories = Inventory.objects.all()
    context = {
        'all_inventories': all_inventories
    }
    return render(request, 'inventory/index.html', context)

def inventory_detail(request, inventory_id, computer_id):
    inventory = get_object_or_404(Inventory, pk=inventory_id)
    computer = get_object_or_404(Computer, pk=computer_id)
    context = {
        'inventory': inventory,
        'computer': computer
    }
 #   url = "/inventory" + str(inventory.id) + "/"
    return render(request, 'inventory/detail.html', context)

def add_inventory(request):
    if request.method == "POST":
        form = inventoryForm(request.POST)
        if form.is_valid():
            form.save()
            url = "/inventory/"
            return HttpResponseRedirect(url)
    else:
        form = inventoryForm()
    context = { 'form': form }
    return render(request, 'inventory/add_inventory.html', context)

def add_computer(request, inventory_id):
    inventory = get_object_or_404(Inventory, pk=inventory_id)
    if request.method == "POST":
        form = computerForm(request.POST)
        form.save()
        url = "/inventory/" + str(inventory_id) + "/"
        return HttpResponseRedirect(url)
    else:
        form = computerForm()
        return render(request, 'inventory/add_computer.html', {})

def edit_computer(request, inventory_id, computer_id):
    computer = get_object_or_404(Computer, pk=computer_id)
    if request.method == "POST":
        form = computerForm(request.POST, instance=computer)
        form.save()
        url = "/inventory/" + str(inventory_id) + "/" + str(computer_id) + "/"
        return HttpResponseRedirect(url)
    else:
        form = computerForm()
        return render(request, 'inventory/edit.html', {})

def delete_computer(request, inventory_id, computer_id):
    computer = get_object_or_404(Computer, pk=computer_id)
    if request.method == "POST":
        computer.delete()
        url = "/inventory/" + str(inventory_id) + "/"
        return HttpResponseRedirect(url)
    else:
        context = {
            'computer': computer
        }
        return render(request, 'inventory/delete_computer.html', context)

        