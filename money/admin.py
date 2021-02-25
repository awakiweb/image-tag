from django.contrib import admin

from .models import Money, ExchangeRate

admin.site.register(Money)
admin.site.register(ExchangeRate)
