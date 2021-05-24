from graphene_django.types import DjangoObjectType

from .models import Brand, Model, Size, Product


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


class ProductTypes(DjangoObjectType):
    class Meta:
        model = Product
