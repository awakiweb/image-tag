import graphene
import graphql_jwt

from finance.mutations import CreateWallet, UpdateWallet, DeleteWallet
from finance.mutations import CreateMovementType, UpdateMovementType, DeleteMovementType
from finance.mutations import CreateMovementAccount, UpdateMovementAccount, DeleteMovementAccount


# ************** MUTATIONS ************** #
# ************** #

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    create_wallet = CreateWallet.Field()
    update_wallet = UpdateWallet.Field()
    delete_wallet = DeleteWallet.Field()

    create_movement_type = CreateMovementType.Field()
    update_movement_type = UpdateMovementType.Field()
    delete_movement_type = DeleteMovementType.Field()

    create_movement_account = CreateMovementAccount.Field()
    update_movement_account = UpdateMovementAccount.Field()
    delete_movement_account = DeleteMovementAccount.Field()
