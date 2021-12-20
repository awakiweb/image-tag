import graphene
from graphene_django.types import ObjectType

from decimal import Decimal
from django.db.models import Sum

from money.models import Money, ExchangeRate
from money.types import MoneyTypes, ExchangeRateTypes

from finance.models import MovementAccount, MovementType
from finance.types import StatementAccount, DashboardType, DashboardTypeDate


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

    # ************** FINANCE ************** #
    # ************** #
    statement_account = graphene.Field(StatementAccount)
    dashboard_type = graphene.List(DashboardType, first_date=graphene.Date(), last_date=graphene.Date())
    dashboard_type_date = graphene.List(DashboardTypeDate, first_date=graphene.Date(), last_date=graphene.Date())

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

        total_income = incomes['total'] or Decimal()
        total_expense = expenses['total'] or Decimal()

        total = total_income - total_expense
        return StatementAccount(income=total_income, expense=total_expense, total=total)

    def resolve_dashboard_type(self, info, **kwargs):
        first_date = kwargs.get('first_date')
        last_date = kwargs.get('last_date')

        movements = MovementAccount.objects.filter(movement_type__type=MovementType.DEPARTURE)

        if first_date and last_date:
            movements = movements.filter(date__gte=first_date, date__lte=last_date)

        all_movements = movements.aggregate(total=Sum('value'))
        movements = movements.values('movement_type__name').annotate(total=Sum('value')).order_by('-total')
        return [DashboardType(category=item['movement_type__name'], total=item['total'], percentage=(item['total']/all_movements['total']) * 100) for item in movements]

    def resolve_dashboard_type_date(self, info, **kwargs):
        first_date = kwargs.get('first_date')
        last_date = kwargs.get('last_date')

        movements = MovementAccount.objects.filter(movement_type__type=MovementType.DEPARTURE)

        if first_date and last_date:
            movements = movements.filter(date__gte=first_date, date__lte=last_date)

        movements = movements.values('movement_type__name', 'date').annotate(total=Sum('value')).order_by('date')
        return [DashboardTypeDate(date=item['date'], category=item['movement_type__name'], total=item['total']) for item in movements]
