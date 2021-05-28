from graphene_django.types import DjangoObjectType

from .models import Money, ExchangeRate


# ************** TYPES MODELS ************** #
# ************** #
class MoneyTypes(DjangoObjectType):
    class Meta:
        model = Money


class ExchangeRateTypes(DjangoObjectType):
    class Meta:
        model = ExchangeRate
