import graphene
from graphql_jwt.decorators import login_required

from money.models import Money
from .models import Wallet, MovementCategory, MovementType, MovementAccount


# ************** INPUT MUTATIONS ************** #
# ************** #
class WalletInput(graphene.InputObjectType):
    money_id = graphene.Int(required=True)
    name = graphene.String(required=True)
    color = graphene.String(required=True)
    start_value = graphene.Decimal(required=True)
    active = graphene.Boolean(required=True)


class MovementTypeInput(graphene.InputObjectType):
    category_id = graphene.Int(required=True)

    type = graphene.String(required=True)
    name = graphene.String(required=True)
    active = graphene.Boolean(required=True)


class MovementAccountInput(graphene.InputObjectType):
    wallet_id = graphene.Int(required=True)
    movement_type_id = graphene.Int(required=True)

    date = graphene.DateTime(required=True)
    value = graphene.Decimal(required=True)
    active = graphene.Boolean(required=True)


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

            wallet_instance = Wallet(
                user=user,
                money=money,
                name=params.name,
                color=params.color,
                start_value=params.start_value,
                active=True
            )

            wallet_instance.save()
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


class CreateMovementType(graphene.Mutation):
    class Arguments:
        params = MovementTypeInput(required=True)

    id = graphene.Int()
    ok = graphene.Boolean()
    message = graphene.String()

    @login_required
    def mutate(self, info, params):
        if params:
            user = info.context.user
            category = MovementCategory.objects.get(pk=params.category_id)

            movement_type_instance = MovementType(
                user=user,
                category=category,
                name=params.name,
                type=params.type,
                active=True
            )

            movement_type_instance.save()
            return CreateMovementType(ok=True, id=movement_type_instance.id, message='Tipo de movimiento creado con exito')
        return CreateMovementType(ok=False, id=0, message='Parametros invalidos')


class UpdateMovementType(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)
        params = MovementTypeInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()

    @login_required
    def mutate(self, info, identify, params=None):
        movement_type_instance = MovementType.objects.get(pk=identify)

        category = MovementCategory.objects.get(pk=params.category_id)

        if movement_type_instance:
            movement_type_instance.name = params.name
            movement_type_instance.type = params.type
            movement_type_instance.active = params.active

            movement_type_instance.category = category

            movement_type_instance.save()
            return UpdateMovementType(ok=True, message='Tipo de movimiento modificada con exito')
        return UpdateMovementType(ok=False, message='Parametros invalidos')


class DeleteMovementType(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)

    ok = graphene.Boolean()
    message = graphene.String()

    @login_required
    def mutate(self, info, identify, params=None):
        movement_type_instance = MovementType.objects.get(pk=identify)

        if movement_type_instance:
            movement_type_instance.delete()
            return DeleteMovementType(ok=True, message='Tipo de movimiento eliminada con exito')
        return DeleteMovementType(ok=False, message='Parametros invalidos')


class CreateMovementAccount(graphene.Mutation):
    class Arguments:
        params = MovementAccountInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()

    @login_required
    def mutate(self, info, params):
        if params:
            wallet = Wallet.objects.get(pk=params.wallet_id)
            movement_type = MovementType.objects.get(pk=params.movement_type_id)

            movement_account_instance = MovementAccount(
                wallet=wallet,
                movement_type=movement_type,
                date=params.date,
                value=params.value,
                active=True
            )

            movement_account_instance.save()
            return CreateMovementAccount(ok=True, message='Movimiento creado con exito')
        return CreateMovementAccount(ok=False, message='Parametros invalidos')


class UpdateMovementAccount(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)
        params = MovementAccountInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()

    @login_required
    def mutate(self, info, identify, params=None):
        movement_account_instance = MovementAccount.objects.get(pk=identify)

        wallet = Wallet.objects.get(pk=params.wallet_id)
        movement_type = MovementType.objects.get(pk=params.movement_type_id)

        if movement_account_instance:
            movement_account_instance.date = params.date
            movement_account_instance.value = params.value
            movement_account_instance.active = params.active

            movement_account_instance.wallet = wallet
            movement_account_instance.movement_type = movement_type

            movement_account_instance.save()
            return UpdateMovementAccount(ok=True, message='Movimiento modificada con exito')
        return UpdateMovementAccount(ok=False, message='Parametros invalidos')


class DeleteMovementAccount(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)

    ok = graphene.Boolean()
    message = graphene.String()

    @login_required
    def mutate(self, info, identify, params=None):
        movement_account_instance = MovementAccount.objects.get(pk=identify)

        if movement_account_instance:
            movement_account_instance.delete()
            return DeleteMovementAccount(ok=True, message='Movimiento eliminada con exito')
        return DeleteMovementAccount(ok=False, message='Parametros invalidos')
