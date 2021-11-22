from django.db import models
from money.models import Money


# Create your models here.
class MovementType(models.Model):
    ENTRY = 'E'
    DEPARTURE = 'S'

    MOVEMENT_CHOICES = [
        (ENTRY, 'Movimiento de Entrada'),
        (DEPARTURE, 'Movimiento de Salida')
    ]

    type = models.CharField(max_length=1, choices=MOVEMENT_CHOICES, default=ENTRY)
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class MovementAccount(models.Model):
    money = models.ForeignKey(Money, related_name='movement_accounts', on_delete=models.CASCADE)
    movement_type = models.ForeignKey(MovementType, related_name='movement_accounts', on_delete=models.CASCADE)

    value = models.FloatField()
    date = models.DateField()

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.movement_type.name)
