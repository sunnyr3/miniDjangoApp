from django import forms
from django.forms import CharField
from django.core import validators
from .models import Computer, Inventory


class inventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['inventory_name']

class computerForm(forms.ModelForm):
    comments = CharField(required = False)
    class Meta:
        model = Computer
        fields = ['manufacturer', "serial_number", 'comments']
