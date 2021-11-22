import graphene
from graphene_django.types import DjangoObjectType


# ************** TYPES MODELS ************** #
# ************** #
class StatementAccount(DjangoObjectType):
    income = graphene.Float()
    expense = graphene.Float()

    total = graphene.Float()
