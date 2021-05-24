from graphene_django.types import DjangoObjectType

from .models import Unit, Color


# ************** TYPES MODELS ************** #
# ************** #
class UnitTypes(DjangoObjectType):
    class Meta:
        model = Unit


class ColorTypes(DjangoObjectType):
    class Meta:
        model = Color
