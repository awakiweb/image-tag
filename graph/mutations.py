import graphene
import graphql_jwt

from finance.mutations import CreateWallet, UpdateWallet, DeleteWallet


# ************** MUTATIONS ************** #
# ************** #

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    create_wallet = CreateWallet.Field()
    update_wallet = UpdateWallet.Field()
    delete_wallet = DeleteWallet.Field()
