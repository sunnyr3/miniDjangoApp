from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Inventory, Computer
from .forms import computerForm, inventoryForm

# List all of the inventories
def index(request):
    all_inventories = Inventory.objects.all()
    context = {
        'all_inventories': all_inventories
    }
    return render(request, 'inventory/index.html', context)

# Show detail info of each computer that the inventory has.
# Including manufacturer, serial number and comments
def inventory_detail(request, inventory_id):
    inventory = get_object_or_404(Inventory, pk=inventory_id)
    computer = Computer.objects.filter(inventory=inventory_id)
    context = {
        'inventory': inventory,
        'computer': computer
    }
    return render(request, 'inventory/inventory_detail.html', context)

# Function to add inventory
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

# Function to add computer
def add_computer(request, inventory_id):
    inventory = get_object_or_404(Inventory, pk=inventory_id)
    if request.method == "POST":
        form = computerForm(request.POST)
        # If the form is valid, then save it and return to the corresponding inventory page
        if form.is_valid():
            comp = form.save(commit=False)
            comp.inventory = Inventory.objects.get(pk=inventory_id)
            comp.save()
            url = "/inventory/" + str(inventory_id) + "/"
            return HttpResponseRedirect(url)
    else:
        form = computerForm()
    context = { 'form': form }
    return render(request, 'inventory/add_computer.html', context)

# Function to edit info of the computer
def edit_computer(request, inventory_id, computer_id):
    computer = get_object_or_404(Computer, pk=computer_id)
    if request.method == "POST":
        form = computerForm(request.POST, instance=computer)
        # If the form is valid, then save it and return to the corresponding inventory page
        if form.is_valid():
            form.save()
            url = "/inventory/" + str(inventory_id) + "/" + str(computer_id) + "/"
            return HttpResponseRedirect(url)
    else:
        form = computerForm()
    context = { 
        'form': form,
        'computer': computer
    }
    return render(request, 'inventory/edit_computer.html', context)

# Function to delete computer
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

        