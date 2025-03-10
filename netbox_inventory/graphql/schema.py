import strawberry
import strawberry_django

from netbox_inventory.models import (
    Asset,
    Supplier,
    Purchase,
    Delivery,
    InventoryItemType,
    InventoryItemGroup,
    Account,
    Department,
    Invoice,
)
from .types import (
    AssetType,
    SupplierType,
    PurchaseType,
    DeliveryType,
    InventoryItemTypeType,
    InventoryItemGroupType,
    InvoiceType,
    AccountType,
    DepartmentType
)


@strawberry.type
class AssetQuery:
    @strawberry.field
    def asset(self, id: int) -> AssetType:
        return Asset.objects.get(pk=id)

    asset_list: list[AssetType] = strawberry_django.field()


@strawberry.type
class SupplierQuery:
    @strawberry.field
    def supplier(self, id: int) -> SupplierType:
        return Supplier.objects.get(pk=id)

    supplier_list: list[SupplierType] = strawberry_django.field()


@strawberry.type
class PurchaseQuery:
    @strawberry.field
    def purchase(self, id: int) -> PurchaseType:
        return Purchase.objects.get(pk=id)

    purchase_list: list[PurchaseType] = strawberry_django.field()


@strawberry.type
class DeliveryQuery:
    @strawberry.field
    def delivery(self, id: int) -> DeliveryType:
        return Delivery.objects.get(pk=id)

    delivery_list: list[DeliveryType] = strawberry_django.field()


@strawberry.type
class InventoryItemTypeQuery:
    @strawberry.field
    def inventory_item_type(self, id: int) -> InventoryItemTypeType:
        return InventoryItemType.objects.get(pk=id)

    inventory_item_type_list: list[InventoryItemTypeType] = strawberry_django.field()


@strawberry.type
class InventoryItemGroupQuery:
    @strawberry.field
    def inventory_item_group(self, id: int) -> InventoryItemGroupType:
        return InventoryItemGroup.objects.get(pk=id)

    inventory_item_group_list: list[InventoryItemGroupType] = strawberry_django.field()


@strawberry.type
class AccountQuery:
    @strawberry.field
    def account(self, id: int) -> AccountType:
        return Account.objects.get(pk=id)

    account_list: list[AccountType] = strawberry_django.field()


@strawberry.type
class DepartmentQuery:
    @strawberry.field
    def department(self, id: int) -> DepartmentType:
        return department.objects.get(pk=id)

    department_list: list[DepartmentType] = strawberry_django.field()


@strawberry.type
class InvoiceQuery:
    @strawberry.field
    def invoice(self, id: int) -> InvoiceType:
        return Invoice.objects.get(pk=id)

    invoice_list: list[InvoiceType] = strawberry_django.field()
