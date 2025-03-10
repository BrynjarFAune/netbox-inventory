from netbox.views import generic
from utilities.query import count_related
from utilities.views import register_model_view
from .. import filtersets, forms, models, tables

# Department views
@register_model_view(models.Department)
class DepartmentView(generic.ObjectView):
    queryset = models.Department.objects.all()

    def get_extra_context(self, request, instance):
        invoices = models.Invoice.objects.filter(department=instance)
        return {
            'invoice_count': invoices.count(),
            'invoice_table': tables.InvoiceTable(invoices, user=request.user),
        }

@register_model_view(models.Department, 'list', path='', detail=False)
class DepartmentListView(generic.ObjectListView):
    queryset = models.Department.objects.annotate(
        invoice_count=count_related(models.Invoice, 'department')
    )
    table = tables.DepartmentTable

@register_model_view(models.Department, 'edit')
@register_model_view(models.Department, 'add', detail=False)
class DepartmentEditView(generic.ObjectEditView):
    queryset = models.Department.objects.all()
    form = forms.DepartmentForm

@register_model_view(models.Department, 'delete')
class DepartmentDeleteView(generic.ObjectDeleteView):
    queryset = models.Department.objects.all()

@register_model_view(models.Department, 'bulk_delete', path='delete', detail=False)
class DepartmentBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Department.objects.all()
    table = tables.DepartmentTable
    default_return_url = 'plugins:netbox_inventory:department_list'

@register_model_view(models.Department, 'bulk_import', path='import', detail=False)
class DepartmentBulkImportView(generic.BulkImportView):
    queryset = models.Department.objects.all()
    model_form = forms.DepartmentImportForm
    table = tables.DepartmentTable
