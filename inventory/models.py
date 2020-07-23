from django.db import models
from product.models import Product


class Store(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Inventory(models.Model):
    store = models.ForeignKey(Store, related_name='inventories', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='inventories', on_delete=models.CASCADE)

    available = models.FloatField()
    stock = models.FloatField()

    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.product.name)


class MovementType(models.Model):
    ENTRY = 'E'
    DEPARTURE = 'S'

    MOVEMENT_CHOICES = [
        (ENTRY, 'Movimiento de Entrada'),
        (DEPARTURE, 'Movimiento de Salida')
    ]

    type = models.CharField(max_length=2, choices=MOVEMENT_CHOICES, default=ENTRY)

    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Movement(models.Model):
    movement_type = models.ForeignKey(MovementType, related_name='movements', on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, related_name='movements', on_delete=models.CASCADE)

    date = models.DateTimeField()
    quantity = models.FloatField()
    description = models.TextField(blank=True, null=True)

    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{} {}".format(self.inventory.product.name, self.movement_type.name)