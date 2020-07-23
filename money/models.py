from django.db import models


class Money(models.Model):
    name = models.CharField(max_length=150)
    symbol = models.CharField(max_length=2)
    principal = models.BooleanField(default=False)

    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class ExchangeRate(models.Model):
    money = models.ForeignKey(Money, related_name='exchange_rates', on_delete=models.CASCADE)
    date = models.DateField()
    value = models.FloatField()

    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.money.name)
