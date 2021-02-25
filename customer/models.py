from django.db import models


class Customer(models.Model):
    identification = models.CharField(max_length=30)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    MALE = 'M'
    FEMALE = 'F'

    GENRE_CHOICES = [
        (MALE, 'Masculino'),
        (FEMALE, 'Femenino')
    ]

    genre = models.CharField(max_length=2, choices=GENRE_CHOICES, default=MALE)
    email = models.CharField(max_length=50, blank=False, null=True)
    phone_number = models.CharField(max_length=25, blank=False, null=True)

    address = models.TextField(blank=False, null=True)
    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
