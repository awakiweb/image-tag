from graphene_django.types import DjangoObjectType

from .models import Brand, Model, Size, Unit, Color, Product


# ************** TYPES MODELS ************** #
# ************** #
class BrandTypes(DjangoObjectType):
    class Meta:
        model = Brand


class ModelTypes(DjangoObjectType):
    class Meta:
        model = Model


class SizeTypes(DjangoObjectType):
    class Meta:
        model = Size


class UnitTypes(DjangoObjectType):
    class Meta:
        model = Unit


class ColorTypes(DjangoObjectType):
    class Meta:
        model = Color


class ProductTypes(DjangoObjectType):
    class Meta:
        model = Product
