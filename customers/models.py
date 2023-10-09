from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
