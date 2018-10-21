from django.db import models
from django.db.models import CharField

class Inventory(models.Model):
    inventory_name = CharField(max_length=100, unique=True)
    
class Computer(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True)
    serial_number = CharField(max_length=100)
    manufacturer = CharField(max_length=100)
    comments = models.TextField(max_length=2000, default="")
    
