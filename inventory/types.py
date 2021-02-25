from graphene_django.types import DjangoObjectType

from .models import Store, Inventory, MovementType, Movement


# ************** TYPES MODELS ************** #
# ************** #
class StoreTypes(DjangoObjectType):
    class Meta:
        model = Store


class InventoryTypes(DjangoObjectType):
    class Meta:
        model = Inventory


class MovementTypeTypes(DjangoObjectType):
    class Meta:
        model = MovementType


class MovementTypes(DjangoObjectType):
    class Meta:
        model = Movement
