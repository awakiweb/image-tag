import graphene
from django.contrib.auth.models import User
from graphql_jwt.decorators import login_required

from money.models import Money
from .models import Wallet


# ************** INPUT MUTATIONS ************** #
# ************** #
class WalletInput(graphene.InputObjectType):
    money_id = graphene.Int(required=True)
    name = graphene.String(required=True)
    color = graphene.String(required=True)
    start_value = graphene.Decimal(required=True)
    active = graphene.Boolean()


# ************** MUTATIONS ************** #
# ************** #
class CreateWallet(graphene.Mutation):
    class Arguments:
        params = WalletInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()

    @login_required
    def mutate(self, info, params):
        if params:
            user = info.context.user
            money = Money.objects.get(pk=params.money_id)

            store_instance = Wallet(
                user=user,
                money=money,
                name=params.name,
                color=params.color,
                start_value=params.start_value,
                active=True
            )

            store_instance.save()
            return CreateWallet(ok=True, message='Wallet creada con exito')
        return CreateWallet(ok=False, message='Parametros invalidos')


class UpdateWallet(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)
        params = WalletInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()

    @login_required
    def mutate(self, info, identify, params=None):
        wallet_instance = Wallet.objects.get(pk=identify)

        if wallet_instance:
            wallet_instance.name = params.name if params.name else wallet_instance.name
            wallet_instance.color = params.color if params.color else wallet_instance.color
            wallet_instance.start_value = params.start_value if params.start_value else wallet_instance.start_value
            wallet_instance.active = params.active if params.active else wallet_instance.active

            wallet_instance.save()
            return UpdateWallet(ok=True, message='Wallet modificada con exito')
        return UpdateWallet(ok=False, message='Parametros invalidos')


class DeleteWallet(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)

    ok = graphene.Boolean()
    message = graphene.String()

    @login_required
    def mutate(self, info, identify, params=None):
        wallet_instance = Wallet.objects.get(pk=identify)

        if wallet_instance:
            wallet_instance.delete()
            return UpdateWallet(ok=True, message='Wallet eliminada con exito')
        return UpdateWallet(ok=False, message='Parametros invalidos')
