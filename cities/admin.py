from django.contrib import admin
from .models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'county')
    list_filter = ('county',)
    list_per_page = 15
