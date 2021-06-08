from django.contrib import admin

from .models import Sale, SaleDetail, Invoice


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('sale_date', 'money', 'status')


@admin.register(SaleDetail)
class SaleDetailAdmin(admin.ModelAdmin):
    list_display = ('sale', 'inventory', 'quantity', 'price', 'active')


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'sale')
