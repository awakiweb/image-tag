from django.contrib import admin
from .models import Store, Inventory, MovementType, Movement


admin.site.register(Store)
admin.site.register(Inventory)
admin.site.register(MovementType)
admin.site.register(Movement)

