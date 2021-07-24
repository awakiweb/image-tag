from django.contrib import admin
from .models import Brand, Model, Size, Product, ProductPrice


admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Size)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'brand', 'model', 'size', 'active')
    list_filter = ('category', 'model', 'size')


@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'price_type', 'price', 'active')
    list_filter = ('product', 'price_type', 'active')
