import graphene
from graphene_django.types import DjangoObjectType

from .models import Brand, Model, Size, Product

from money.types import MoneyTypes


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

    purchase_money = graphene.Field(type=MoneyTypes)
    sale_money = graphene.Field(type=MoneyTypes)

    class Meta:
        model = Product

    def resolve_purchase_price(self, info):
        return self.get_purchase_price()

    def resolve_sale_price(self, info):
        return self.get_sale_price()

    def resolve_purchase_money(self, info):
        return self.get_purchase_money()

    def resolve_sale_money(self, info):
        return self.get_sale_money()
