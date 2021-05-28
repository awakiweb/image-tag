from graphene_django.types import DjangoObjectType

from .models import Sale, SaleDetail, Invoice


# ************** TYPES MODELS ************** #
# ************** #
class SaleTypes(DjangoObjectType):
    class Meta:
        model = Sale


class SaleDetailTypes(DjangoObjectType):
    class Meta:
        model = SaleDetail


class InvoiceTypes(DjangoObjectType):
    class Meta:
        model = Invoice
