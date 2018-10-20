from django.contrib import admin

from .models import Inventory, Computer

admin.site.register(Inventory)
admin.site.register(Computer)