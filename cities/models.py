from django.db import models

from counties.models import County


class City(models.Model):
    name = models.CharField(max_length=150)
    county = models.ForeignKey(County, related_name='cities', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return "{}".format(self.name)
