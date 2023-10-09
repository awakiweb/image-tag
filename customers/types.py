from graphene_django.types import DjangoObjectType
from .models import Customer


class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
