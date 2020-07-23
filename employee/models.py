from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    user = models.ForeignKey(User, related_name='employees', on_delete=models.CASCADE)

    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)
