from netbox.views import generic
from .. import filtersets, forms, models, tables
from django.db.models import Count

# Account views
class AccountView(generic.ObjectView):
    queryset = models.Account.objects.all()

    def get_extra_context(self, request, instance):
        table = tables.InvoiceTable(instance.invoices.all())
        table.configure(request)

        return {
            'invoice_table': table
        }

class AccountListView(generic.ObjectListView):
    queryset = models.Account.objects.annotate(
        invoice_count=Count('invoices')
    )
    table = tables.AccountTable

class AccountEditView(generic.ObjectEditView):
    queryset = models.Account.objects.all()
    form = forms.AccountForm

class AccountDeleteView(generic.ObjectDeleteView):
    queryset = models.Account.objects.all()

class AccountBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Account.objects.all()
    table = tables.AccountTable
    default_return_url = 'plugins:netbox_inventory:account_list'

class AccountBulkImportView(generic.BulkImportView):
    queryset = models.Account.objects.all()
    model_form = forms.AccountImportForm
    table = tables.AccountTable
