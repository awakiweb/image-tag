from django.db import models


class ExcelColumn(models.Model):
    label = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    key = models.CharField(max_length=250)

    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    class Meta:
        ordering = ('-updated_at',)

    def __str__(self):
        return "{}".format(self.label)
