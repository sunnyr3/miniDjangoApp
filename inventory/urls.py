from django.conf.urls import url

from . import views

app_name = 'inventory'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # inventory/inventory_id/
    url(r'^inventory/(?P<inventory_id>[0-9]+)/$', views.inventory_detail, name="inventory_detail"),
    # inventory/add_inventory
    url(r'^inventory/add_inventory/$', views.add_inventory, name='add_inventory'),
    # inventory/inventory_id/add_computer
    url(r'^inventory/(?P<inventory_id>[0-9]+)/add_computer/$', views.add_computer, name="add_computer"),
    # inventory/inventory_id/computer_id/edit_computer
    url(r'^inventory/(?P<inventory_id>[0-9]+)/(?P<computer_id>[0-9]+)/edit_computer/$', views.edit_computer, name="edit_computer"),
    # inventory/inventory_id/computer_id/delete_computer
    url(r'^inventory/(?P<inventory_id>[0-9]+)/(?P<computer_id>[0-9]+)/delete_computer/$', views.delete_computer, name="delete_computer")
]