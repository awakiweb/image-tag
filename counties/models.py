from django.db import models


class County(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'counties'

    def __str__(self):
        return "{}".format(self.name)
