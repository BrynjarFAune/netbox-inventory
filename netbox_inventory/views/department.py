from netbox.views import generic
from .. import filtersets, forms, models, tables
from django.db.models import Count

# Department views
class DepartmentView(generic.ObjectView):
    queryset = models.Department.objects.all()

    def get_extra_context(self, request, instance):
        table = tables.InvoiceTable(instance.invoices.all())
        table.configure(request)

        return {
            'invoice_table': table
        }

class DepartmentListView(generic.ObjectListView):
    queryset = models.Department.objects.annotate(
        invoice_count=Count('invoices')
    )
    table = tables.DepartmentTable

class DepartmentEditView(generic.ObjectEditView):
    queryset = models.Department.objects.all()
    form = forms.DepartmentForm

class DepartmentDeleteView(generic.ObjectDeleteView):
    queryset = models.Department.objects.all()

class DepartmentBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Department.objects.all()
    table = tables.DepartmentTable
    default_return_url = 'plugins:netbox_inventory:department_list'

class DepartmentBulkImportView(generic.BulkImportView):
    queryset = models.Department.objects.all()
    model_form = forms.DepartmentImportForm
    table = tables.DepartmentTable
