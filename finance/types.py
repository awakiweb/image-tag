import graphene
from graphene_django.types import ObjectType


# ************** TYPES MODELS ************** #
# ************** #
class StatementAccount(ObjectType):
    income = graphene.Float()
    expense = graphene.Float()
    total = graphene.Float()
