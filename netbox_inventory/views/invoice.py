"""
Processing requests, usually has an assocuated URL and handles HTTP types like POST, GET, ...
"""
from netbox.views import generic
from .. import filtersets, forms, models, tables
from django.db.models import Count

# Invoice views
class InvoiceView(generic.ObjectView):
    queryset = models.Invoice.objects.all()

class InvoiceListView(generic.ObjectListView):
    queryset = models.Invoice.objects.all()
    table = tables.InvoiceTable
    filterset = filtersets.InvoiceFilterSet
    filterset_form = forms.InvoiceFilterForm

class InvoiceEditView(generic.ObjectEditView):
    queryset = models.Invoice.objects.all()
    form = forms.InvoiceForm

class InvoiceDeleteView(generic.ObjectDeleteView):
    queryset = models.Invoice.objects.all()

class InvoiceBulkImportView(generic.BulkImportView):
    queryset = models.Invoice.objects.all()
    model_form = forms.InvoiceImportForm
    table = tables.InvoiceTable

class InvoiceBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Invoice.objects.all()
    table = tables.InvoiceTable
    default_return_url = 'plugins:netbox_inventory:invoice_list'

class InvoiceBulkEditView(generic.BulkEditView):
    queryset = models.Invoice.objects.all()
    form = forms.InvoiceBulkEditForm
    table = tables.InvoiceTable
    default_return_url = 'plugins:netbox_inventory:invoice_list'
