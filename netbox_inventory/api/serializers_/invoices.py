from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from .deliveries import PurchaseSerializer
from netbox_inventory.models import Invoice, Department, Account

class DepartmentSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_inventory-api:department-detail'
    )
    invoice_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Department
        fields = (
            'id', 'url', 'display', 'name', 'department_id', 'tags', 'custom_fields', 'created', 'last_updated', 'invoice_count'
        )
        brief_fields = ('id', 'url', 'display', 'name', 'department_id')

class AccountSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_inventory-api:account-detail'
    )
    invoice_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Account
        fields = (
            'id', 'url', 'display', 'name', 'number', 'comments', 'tags', 'custom_fields', 'created', 'last_updated', 'invoice_count'
        )
        brief_fields = ('id', 'url', 'display', 'name', 'number')

class InvoiceSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_inventory-api:invoice-detail'
    )
    account = AccountSerializer(nested=True)
    department = DepartmentSerializer(nested=True)
    purchase = PurchaseSerializer(nested=True)

    class Meta:
        model = Invoice
        fields = (
            'id', 'url', 'display', 'invoice_id', 'department', 'account', 'purchase', 'amount', 'currency', 'nok_value', 'approval_date', 'defined_period', 'period', 'comments', 'tags', 'custom_fields', 'created', 'last_updated'
        )
        brief_fields = ('id', 'url', 'display', 'department', 'account', 'purchase', 'currency', 'amount', 'department_id')
