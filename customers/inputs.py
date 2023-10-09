import graphene


class CustomerInput(graphene.InputObjectType):
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    email = graphene.String(required=True)
    phone_number = graphene.String(required=True)
    title = graphene.String(required=False)
    company_name = graphene.String(required=False)
