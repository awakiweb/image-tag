import graphene
from graphene_django.types import ObjectType


# ************** TYPES MODELS ************** #
# ************** #
class StatementAccount(ObjectType):
    income = graphene.Float()
    expense = graphene.Float()
    total = graphene.Float()


class DashboardType(ObjectType):
    total = graphene.Float()
    category = graphene.String()
    percentage = graphene.Float()


class DashboardTypeDate(ObjectType):
    date = graphene.Date()
    total = graphene.Float()
    category = graphene.String()
