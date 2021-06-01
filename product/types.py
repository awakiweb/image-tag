import graphene
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
    purchase_price = graphene.Float()
    sale_price = graphene.Float()

    class Meta:
        model = Product

    def resolve_purchase_price(self, info):
        return self.get_purchase_price()

    def resolve_sale_price(self, info):
        return self.get_sale_price()
