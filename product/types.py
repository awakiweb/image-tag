import graphene
from graphene_django.types import DjangoObjectType

from .models import Brand, Model, Size, Product, ProductPrice


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


class ProductPriceTypes(DjangoObjectType):
    class Meta:
        model = ProductPrice


class ProductTypes(DjangoObjectType):
    purchase_price = graphene.Field(type=ProductPriceTypes)
    sale_price = graphene.Field(type=ProductPriceTypes)

    class Meta:
        model = Product

    def resolve_purchase_price(self, info):
        return self.get_purchase_price()

    def resolve_sale_price(self, info):
        return self.get_sale_price()

