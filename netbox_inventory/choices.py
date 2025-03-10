from utilities.choices import ChoiceSet


#
# Assets
#

class AssetStatusChoices(ChoiceSet):
    key = 'Asset.status'

    CHOICES = [
        ('stored', 'Stored', 'green'),
        ('used', 'Used', 'blue'),
        ('retired', 'Retired', 'gray'),
    ]


class HardwareKindChoices(ChoiceSet):
    CHOICES = [
        ('device', 'Device'),
        ('module', 'Module'),
        ('inventoryitem', 'Inventory Item'),
        ('rack', 'Rack'),
    ]


#
# Deliveries
#

class PurchaseStatusChoices(ChoiceSet):
    key = 'Purchase.status'

    CHOICES = [
        ('open', 'Open', 'cyan'),
        ('partial', 'Partial', 'blue'),
        ('closed', 'Closed', 'green'),
    ]

#
# Invoices
#

class CurrencyChoices(ChoiceSet):
    key = 'Invoice.currency'

    CHOICES = [
        ('nok', 'NOK'),
        ('dkk', 'DKK'),
        ('eur', 'EUR'),
        ('usd', 'USD'),
    ]
