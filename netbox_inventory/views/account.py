from netbox.views import generic
from utilities.query import count_related
from utilities.views import register_model_view
from .. import filtersets, forms, models, tables

# Account views
@register_model_view(models.Account)
class AccountView(generic.ObjectView):
    queryset = models.Account.objects.all()

    def get_extra_context(self, request, instance):
        invoices = models.Invoice.objects.filter(account=instance)
        return {
            'invoice_count': invoices.count(),
            'invoice_table': tables.InvoiceTable(invoices, user=request.user),
        }

@register_model_view(models.Account, 'list', path='', detail=False)
class AccountListView(generic.ObjectListView):
    queryset = models.Account.objects.annotate(
        invoice_count=count_related(models.Invoice, 'account')
    )
    table = tables.AccountTable

@register_model_view(models.Account, 'edit')
@register_model_view(models.Account, 'add', detail=False)
class AccountEditView(generic.ObjectEditView):
    queryset = models.Account.objects.all()
    form = forms.AccountForm

@register_model_view(models.Account, 'delete')
class AccountDeleteView(generic.ObjectDeleteView):
    queryset = models.Account.objects.all()

@register_model_view(models.Account, 'bulk_delete', path='delete', detail=False)
class AccountBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Account.objects.all()
    table = tables.AccountTable
    default_return_url = 'plugins:netbox_inventory:account_list'

@register_model_view(models.Account, 'bulk_import', path='import', detail=False)
class AccountBulkImportView(generic.BulkImportView):
    queryset = models.Account.objects.all()
    model_form = forms.AccountImportForm
    table = tables.AccountTable
