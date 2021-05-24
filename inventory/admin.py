from django.contrib import admin
from .models import Store, Inventory, MovementType, Movement


admin.site.register(Store)
admin.site.register(MovementType)
admin.site.register(Movement)


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'unit', 'color', 'available', 'stock')
    list_filter = ('product', 'unit', 'color')
