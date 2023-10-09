from django.contrib import admin
from .models import ExcelColumn


@admin.register(ExcelColumn)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('label', 'name', 'key', 'id', 'active')
