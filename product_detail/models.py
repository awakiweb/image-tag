from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=150)
    symbol = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)

    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Color(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)
