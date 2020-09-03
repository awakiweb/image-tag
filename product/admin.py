from django.contrib import admin
from .models import Category, Brand, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'parent', 'active')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand)
admin.site.register(Product)
