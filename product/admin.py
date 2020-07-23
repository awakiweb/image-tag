from django.contrib import admin
from .models import Category, Subcategory, Brand, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'active')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory)
admin.site.register(Brand)
admin.site.register(Product)
