from django.contrib import admin

from .models import MovementCategory, MovementType, Wallet, MovementAccount


@admin.register(MovementCategory)
class MovementCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'active')


@admin.register(MovementType)
class MovementTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'type', 'category', 'active')


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'name', 'active')


@admin.register(MovementAccount)
class MovementAccountAdmin(admin.ModelAdmin):
    list_filter = ('movement_type',)
    list_display = ('movement_type', 'id', 'wallet', 'money', 'date', 'value')
