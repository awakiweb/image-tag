from django.contrib import admin
from .models import Brand, Model, Size, Unit, Color, Product, ProductPrice


admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Size)
admin.site.register(Unit)
admin.site.register(Color)
admin.site.register(Product)
admin.site.register(ProductPrice)
