from netbox.views import generic
from utilities.views import register_model_view
from .. import filtersets, forms, models, tables

# Invoice views
@register_model_view(models.Invoice)
class InvoiceView(generic.ObjectView):
    queryset = models.Invoice.objects.all()

@register_model_view(models.Invoice, 'list', path='', detail=False)
class InvoiceListView(generic.ObjectListView):
    queryset = models.Invoice.objects.all()
    table = tables.InvoiceTable
    filterset = filtersets.InvoiceFilterSet
    filterset_form = forms.InvoiceFilterForm

@register_model_view(models.Invoice, 'edit')
@register_model_view(models.Invoice, 'add', detail=False)
class InvoiceEditView(generic.ObjectEditView):
    queryset = models.Invoice.objects.all()
    form = forms.InvoiceForm

@register_model_view(models.Invoice, 'delete')
class InvoiceDeleteView(generic.ObjectDeleteView):
    queryset = models.Invoice.objects.all()

@register_model_view(models.Invoice, 'bulk_import', path='import', detail=False)
class InvoiceBulkImportView(generic.BulkImportView):
    queryset = models.Invoice.objects.all()
    model_form = forms.InvoiceImportForm
    table = tables.InvoiceTable

@register_model_view(models.Invoice, 'bulk_delete', path='delete', detail=False)
class InvoiceBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Invoice.objects.all()
    table = tables.InvoiceTable

@register_model_view(models.Invoice, 'bulk_edit', path='edit', detail=False)
class InvoiceBulkEditView(generic.BulkEditView):
    queryset = models.Invoice.objects.all()
    form = forms.InvoiceBulkEditForm
    table = tables.InvoiceTable
