from django.contrib import admin

from .models import MovementType, MovementAccount


@admin.register(MovementType)
class MoneyAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'type', 'active')


@admin.register(MovementAccount)
class MoneyAdmin(admin.ModelAdmin):
    list_filter = ('movement_type',)
    list_display = ('movement_type', 'id', 'money', 'date', 'value')

