from django.contrib import admin
from .models import Brand, Model, Size, Unit, Color, Product, ProductPrice


admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Size)
admin.site.register(Unit)
admin.site.register(Color)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'model', 'unit', 'size', 'color', 'active')
    list_filter = ('category', 'model', 'unit', 'size', 'color')


@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'price_type', 'price', 'active')
    list_filter = ('product', 'price_type', 'active')
