from django.contrib import admin

from .models import Money, ExchangeRate

admin.site.register(ExchangeRate)


@admin.register(Money)
class MoneyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'symbol', 'principal', 'active')
