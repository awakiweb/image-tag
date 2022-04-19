import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Wallet, MovementType, MovementCategory, MovementAccount


# ************** TYPES MODELS ************** #
# ************** #
class MovementCategoryTypes(DjangoObjectType):
    class Meta:
        model = MovementCategory


class MovementTypeTypes(DjangoObjectType):
    class Meta:
        model = MovementType


class WalletTypes(DjangoObjectType):
    total_departures = graphene.Float()
    total_entries = graphene.Float()
    total = graphene.Float()

    class Meta:
        model = Wallet

    def resolve_total_departures(self, info):
        return self.get_departures()

    def resolve_total_entries(self, info):
        return self.get_entries()

    def resolve_total(self, info):
        return self.get_total()


class MovementAccountTypes(DjangoObjectType):
    class Meta:
        model = MovementAccount


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
