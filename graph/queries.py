import datetime
import graphene
from graphene_django.types import ObjectType

from decimal import Decimal
from django.db.models import Sum
from graphql_jwt.decorators import login_required

from money.models import Money, ExchangeRate
from money.types import MoneyTypes, ExchangeRateTypes

from finance.models import MovementCategory, MovementType, Wallet, MovementAccount, MovementType
from finance.types import MovementCategoryTypes, MovementTypeTypes, WalletTypes, MovementAccountTypes, StatementAccount, DashboardType, DashboardTypeDate


# ************** QUERY MODELS ************** #
# ************** #
class Query(ObjectType):
    # ************** MONEYS ************** #
    # ************** #
    not_principal_money = graphene.List(MoneyTypes)
    principal_money = graphene.Field(MoneyTypes)
    money = graphene.Field(MoneyTypes, id=graphene.Int(required=True))
    moneys = graphene.List(MoneyTypes)

    exchange_rate = graphene.Field(ExchangeRateTypes, id=graphene.Int(required=True))
    exchange_rates = graphene.List(ExchangeRateTypes)

    # ************** FINANCE ************** #
    # ************** #
    wallet = graphene.Field(WalletTypes, id=graphene.Int(required=True))
    wallets = graphene.List(WalletTypes)

    movement_categories = graphene.List(MovementCategoryTypes)
    movement_types = graphene.List(MovementTypeTypes)

    movement_account = graphene.Field(MovementAccountTypes, id=graphene.Int(required=True))
    movement_accounts = graphene.List(MovementAccountTypes, wallet_id=graphene.Int(required=True))

    statement_account = graphene.Field(StatementAccount)
    dashboard_type = graphene.List(DashboardType, first_date=graphene.Date(), last_date=graphene.Date())
    dashboard_type_date = graphene.List(DashboardTypeDate, first_date=graphene.Date(), last_date=graphene.Date())
    dashboard_type_month = graphene.List(DashboardTypeDate, month=graphene.Int(), year=graphene.Int())

    # ************** MONEYS ************** #
    # ************** #
    @login_required
    def resolve_not_principal_money(self, info, **kwargs):
        return Money.objects.filter(principal=False)

    @login_required
    def resolve_principal_money(self, info, **kwargs):
        return Money.objects.get(principal=True)

    @login_required
    def resolve_money(self, info, **kwargs):
        return Money.objects.get(pk=kwargs.get('id'), active=True)

    @login_required
    def resolve_moneys(self, info, **kwargs):
        return Money.objects.filter(active=True)

    @login_required
    def resolve_exchange_rate(self, info, **kwargs):
        return ExchangeRate.objects.get(pk=kwargs.get('id'))

    @login_required
    def resolve_wallet(self, info, **kwargs):
        user = info.context.user
        return Wallet.objects.get(user=user, pk=kwargs.get('id'), active=True)

    @login_required
    def resolve_wallets(self, info, **kwargs):
        user = info.context.user
        return Wallet.objects.filter(user=user, active=True)

    @login_required
    def resolve_movement_categories(self, info, **kwargs):
        return MovementCategory.objects.filter(active=True)

    @login_required
    def resolve_movement_types(self, info, **kwargs):
        user = info.context.user
        return MovementType.objects.filter(user=user, active=True)

    @login_required
    def resolve_movement_account(self, info, **kwargs):
        return MovementAccount.objects.get(pk=kwargs.get('id'), active=True)

    @login_required
    def resolve_movement_accounts(self, info, **kwargs):
        return MovementAccount.objects.filter(wallet_id=kwargs.get('wallet_id'), active=True)

    @login_required
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

    def resolve_dashboard_type_month(self, info, **kwargs):
        month = kwargs.get('month')
        year = kwargs.get('year')

        movements = MovementAccount.objects.filter(movement_type__type=MovementType.DEPARTURE)

        if month and year:
            movements = movements.filter(date__month=month, date__year=year)

        movements = movements.values('movement_type__name', 'date__month', 'date__year').annotate(total=Sum('value')).order_by('-total', 'date__month', 'date__year')
        return [DashboardTypeDate(date=datetime.date(year=item['date__year'], month=item['date__month'], day=1), category=item['movement_type__name'], total=item['total']) for item in movements]
