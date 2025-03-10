from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.apps import apps

from netbox.models import NetBoxModel
from netbox.models.features import ImageAttachmentsMixin

from ..choices import CurrencyChoices
from .deliveries import Purchase


class Account(NetBoxModel):
    name = models.CharField(
        max_length=100
    )
    number = models.PositiveIntegerField()
    comments = models.TextField(
        blank=True
    )
    class Meta:
        ordering = ('number', 'name')
    def __str__(self):
        return f'{self.number} - {self.name}'
    def get_absolute_url(self):
        return reverse('plugins:netbox_inventory:account', kwargs={'pk': self.pk})

class Department(NetBoxModel):
    name = models.CharField(
        max_length=100
    )
    department_id = models.PositiveIntegerField()
    def get_absolute_url(self):
        return reverse('plugins:netbox_inventory:department', kwargs={'pk': self.pk})
    def __str__(self):
        return f'{self.department_id} - {self.name}'

class Invoice(NetBoxModel, ImageAttachmentsMixin):
    invoice_id = models.PositiveIntegerField()
    comments = models.TextField(
        blank=True,
        null=True,
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    nok_value = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    approval_date = models.DateField(
        blank=True,
        null=True,
    )
    account = models.ForeignKey(
        to=Account,
        on_delete=models.PROTECT,
        related_name='invoices'
    )
    currency = models.CharField(
        max_length=10,
        choices=CurrencyChoices,
        default='nok'
    )
    department = models.ForeignKey(
        to=Department,
        on_delete=models.PROTECT,
        related_name='invoices'
    )
    purchase = models.OneToOneField(
        'Purchase',
        on_delete=models.SET_NULL,
        related_name='related_invoice',
        null=True,
        blank=True
    )
    defined_period = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    period = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    clone_fields = [
        'approval_date', 'account', 'department', 'currency', 'defined_period', 'period'
    ]

    class Meta:
        ordering = ('approval_date', 'invoice_id')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        Purchase = apps.get_model('netbox_inventory', 'Purchase')

        if self.purchase:
            if self.purchase.invoice != self.id:
                self.purchase.invoice = self
                self.purchase.save()
        else:
            existing_purchase = Purchase.objects.filter(invoice=self).first()
            if existing_purchase:
                existing_purchase.invoice = None
                existing_purchase.save()


    def __str__(self):
        return f'{self.invoice_id}'

    def get_absolute_url(self):
        return reverse('plugins:netbox_inventory:invoice', args=[self.pk])
