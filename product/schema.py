import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from .models import Brand, Model, Size, Unit, Color, Product, ProductPrice


# ************** TYPES MODELS ************** #
# ************** #
class BrandType(DjangoObjectType):
    class Meta:
        model = Brand


class ModelType(DjangoObjectType):
    class Meta:
        model = Model


class SizeType(DjangoObjectType):
    class Meta:
        model = Size


class UnitType(DjangoObjectType):
    class Meta:
        model = Unit


class ColorType(DjangoObjectType):
    class Meta:
        model = Color


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class ProductPriceType(DjangoObjectType):
    class Meta:
        model = ProductPrice
