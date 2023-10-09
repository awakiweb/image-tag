import graphene
import graphql_jwt

from projects.mutations import CreateProject, UpdateProject, DeleteProject, ActivateProject, CreateProjectFile
from customers.mutations import CreateCustomer


# ************** MUTATIONS ************** #
# ************** #

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    create_project = CreateProject.Field()
    update_project = UpdateProject.Field()
    delete_project = DeleteProject.Field()
    activate_project = ActivateProject.Field()

    create_project_file = CreateProjectFile.Field()

    create_customer = CreateCustomer.Field()

