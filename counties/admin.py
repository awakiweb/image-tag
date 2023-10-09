from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.contrib import admin

from .models import County


@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'view_cities_link')
    list_per_page = 15

    def view_cities_link(self, obj):
        count = obj.cities.count()
        url = (
            reverse("admin:%s_%s_changelist" % ('cities', 'city'),)
            + "?"
            + urlencode({"county__id__exact": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Cities</a>', url, count)

    view_cities_link.short_description = "Cities"
