from graphene_django.types import DjangoObjectType

from .models import Customer


# ************** TYPES MODELS ************** #
# ************** #
class CustomerTypes(DjangoObjectType):
    class Meta:
        model = Customer
