from django.urls import include, path

from utilities.urls import get_model_urls
from netbox.views.generic import ObjectChangeLogView
from . import views
from .models.invoices import *


urlpatterns = (
    # InventoryItemGroups
    path('inventory-item-groups/', include(get_model_urls('netbox_inventory', 'inventoryitemgroup', detail=False))),
    path('inventory-item-groups/<int:pk>/', include(get_model_urls('netbox_inventory', 'inventoryitemgroup'))),

    # InventoryItemTypes
    path('inventory-item-types/', include(get_model_urls('netbox_inventory', 'inventoryitemtype', detail=False))),
    path('inventory-item-types/<int:pk>/', include(get_model_urls('netbox_inventory', 'inventoryitemtype'))),

    # Assets
    path('assets/', include(get_model_urls('netbox_inventory', 'asset', detail=False))),
    path('assets/<int:pk>/', include(get_model_urls('netbox_inventory', 'asset'))),
    path('assets/<int:pk>/assign/', views.AssetAssignView.as_view(), name='asset_assign'),
    path('assets/device/create/', views.AssetDeviceCreateView.as_view(), name='asset_device_create'),
    path('assets/module/create/', views.AssetModuleCreateView.as_view(), name='asset_module_create'),
    path('assets/inventory-item/create/', views.AssetInventoryItemCreateView.as_view(), name='asset_inventoryitem_create'),
    path('assets/rack/create/', views.AssetRackCreateView.as_view(), name='asset_rack_create'),
    path('assets/device/<int:pk>/reassign/', views.AssetDeviceReassignView.as_view(), name='asset_device_reassign'),
    path('assets/module/<int:pk>/reassign/', views.AssetModuleReassignView.as_view(), name='asset_module_reassign'),
    path('assets/inventoryitem/<int:pk>/reassign/', views.AssetInventoryItemReassignView.as_view(), name='asset_inventoryitem_reassign'),
    path('assets/rack/<int:pk>/reassign/', views.AssetRackReassignView.as_view(), name='asset_rack_reassign'),

    # Suppliers
    path('suppliers/', include(get_model_urls('netbox_inventory', 'supplier', detail=False))),
    path('suppliers/<int:pk>/', include(get_model_urls('netbox_inventory', 'supplier'))),

    # Purchases
    path('purchases/', include(get_model_urls('netbox_inventory', 'purchase', detail=False))),
    path('purchases/<int:pk>/', include(get_model_urls('netbox_inventory', 'purchase'))),

    # Deliveries
    path('deliveries/', include(get_model_urls('netbox_inventory', 'delivery', detail=False))),
    path('deliveries/<int:pk>/', include(get_model_urls('netbox_inventory', 'delivery'))),

    # Invoices
    path('invoices/', views.InvoiceListView.as_view(), name='invoice_list'),
    path('invoices/add/', views.InvoiceEditView.as_view(), name='invoice_add'),
    path('invoices/<int:pk>/', views.InvoiceView.as_view(), name='invoice'),
    path('invoices/<int:pk>/edit/', views.InvoiceEditView.as_view(), name='invoice_edit'),
    path('invoices/<int:pk>/delete/', views.InvoiceDeleteView.as_view(), name='invoice_delete'),
    path('invoices/bulk-delete', views.InvoiceBulkDeleteView.as_view(), name='invoice_bulk_delete'),
    path('invoices/import/', views.InvoiceBulkImportView.as_view(), name='invoice_import'),
    path('invoices/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='invoice_changelog', kwargs={
        'model': Invoice
    }),

    # Accounts
    path('accounts/', views.AccountListView.as_view(), name='account_list'),
    path('accounts/add/', views.AccountEditView.as_view(), name='account_add'),
    path('accounts/<int:pk>/', views.AccountView.as_view(), name='account'),
    path('accounts/<int:pk>/edit/', views.AccountEditView.as_view(), name='account_edit'),
    path('accounts/<int:pk>/delete/', views.AccountDeleteView.as_view(), name='account_delete'),
    path('accounts/bulk-delete', views.AccountBulkDeleteView.as_view(), name='account_bulk_delete'),
    path('accounts/import/', views.AccountBulkImportView.as_view(), name='account_import'),
    path('accounts/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='account_changelog', kwargs={
        'model': Account
    }),

    # Departments
    path('departments/', views.DepartmentListView.as_view(), name='department_list'),
    path('departments/add/', views.DepartmentEditView.as_view(), name='department_add'),
    path('departments/<int:pk>/', views.DepartmentView.as_view(), name='department'),
    path('departments/<int:pk>/edit/', views.DepartmentEditView.as_view(), name='department_edit'),
    path('departments/<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department_delete'),
    path('departments/bulk-delete', views.DepartmentBulkDeleteView.as_view(), name='department_bulk_delete'),
    path('departments/import/', views.DepartmentBulkImportView.as_view(), name='department_import'),
    path('departments/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='department_changelog', kwargs={
        'model': Department
    }),
)
