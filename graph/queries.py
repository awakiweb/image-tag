import graphene
from graphene_django.types import ObjectType

from decimal import Decimal
from django.db.models import Sum

from money.models import Money, ExchangeRate
from money.types import MoneyTypes, ExchangeRateTypes

from finance.models import MovementAccount, MovementType
from finance.types import StatementAccount


# ************** QUERY MODELS ************** #
# ************** #
class Query(ObjectType):
    # ************** MONEYS ************** #
    # ************** #
    not_principal_money = graphene.List(MoneyTypes)
    principal_money = graphene.Field(MoneyTypes)
    money = graphene.Field(MoneyTypes, id=graphene.Int())
    moneys = graphene.List(MoneyTypes)

    exchange_rate = graphene.Field(ExchangeRateTypes, id=graphene.Int())
    exchange_rates = graphene.List(ExchangeRateTypes)

    # ************** MONEYS ************** #
    # ************** #
    statement_account = graphene.Field(StatementAccount)

    # ************** MONEYS ************** #
    # ************** #
    def resolve_not_principal_money(self, info, **kwargs):
        return Money.objects.filter(principal=False)

    def resolve_principal_money(self, info, **kwargs):
        return Money.objects.get(principal=True)

    def resolve_money(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Money.objects.get(pk=identity)

        return None

    def resolve_moneys(self, info, **kwargs):
        return Money.objects.all()

    def resolve_exchange_rate(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return ExchangeRate.objects.get(pk=identity)

        return None

    def resolve_exchange_rates(self, info, **kwargs):
        return ExchangeRate.objects.all()

    def resolve_statement_account(self, info, **kwargs):
        incomes = MovementAccount.objects.filter(movement_type__type=MovementType.ENTRY).aggregate(total=Sum('value'))
        expenses = MovementAccount.objects.filter(movement_type__type=MovementType.DEPARTURE).aggregate(total=Sum('value'))

        total = incomes.total - expenses.total
        return StatementAccount(incomes=incomes.total, expenses=expenses.total, total=total)
