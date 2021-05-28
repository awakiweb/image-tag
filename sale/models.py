from django.db import models

from money.models import Money
from customer.models import Customer
from inventory.models import Inventory


class Sale(models.Model):
    money = models.ForeignKey(Money, related_name='sales', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='sales', null=True, blank=True, on_delete=models.CASCADE)

    CREDIT = 'CR'
    CASH = 'CO'

    TYPE_CHOICES = [
        (CREDIT, 'VENTA AL CREDITO'),
        (CASH, 'VENTA AL CONTADO')
    ]

    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=CASH)
    sale_date = models.DateField()
    status = models.IntegerField()

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)


class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, related_name='sale_details', on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, related_name='sale_details', on_delete=models.CASCADE)

    price = models.FloatField()
    quantity = models.FloatField()
    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)


class Invoice(models.Model):
    sale = models.ForeignKey(Sale, related_name='invoices', on_delete=models.CASCADE)
    money = models.ForeignKey(Money, related_name='invoices', on_delete=models.CASCADE)

    PAYMENT_CARD = 'PC'
    CASH = 'C'

    TYPE_CHOICES = [
        (PAYMENT_CARD, 'Pago con Tarjeta'),
        (CASH, 'Pago con Efectivo')
    ]

    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=CASH)
    amount = models.FloatField()

    invoice_date = models.DateField()
    status = models.IntegerField()

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)
