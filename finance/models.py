from django.db import models
from money.models import Money
from django.contrib.auth.models import User


class MovementCategory(models.Model):
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class MovementType(models.Model):
    ENTRY = 'E'
    DEPARTURE = 'S'

    MOVEMENT_CHOICES = [
        (ENTRY, 'Movimiento de Entrada'),
        (DEPARTURE, 'Movimiento de Salida')
    ]

    type = models.CharField(max_length=1, choices=MOVEMENT_CHOICES, default=ENTRY)
    category = models.ForeignKey(MovementCategory, related_name='movement_types', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Wallet(models.Model):
    user = models.ForeignKey(User, related_name='wallets', on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    start_value = models.FloatField(default=0)
    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class MovementAccount(models.Model):
    money = models.ForeignKey(Money, related_name='movement_accounts', on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, related_name='movement_accounts', on_delete=models.CASCADE)
    movement_type = models.ForeignKey(MovementType, related_name='movement_accounts', on_delete=models.CASCADE)

    date = models.DateField()
    value = models.FloatField()
    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.movement_type.name)
