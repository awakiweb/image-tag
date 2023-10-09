import graphene

from .inputs import CustomerInput
from .models import Customer


class CreateCustomer(graphene.Mutation):
    class Arguments:
        params = CustomerInput(required=True)

    id = graphene.Int()
    ok = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, params):
        if not params:
            return CreateCustomer(id=0, ok=False, message='Params are invalid')

        new_instance = Customer(
            first_name=params.first_name,
            last_name=params.last_name,
            email=params.email,
            phone_number=params.phone_number,
            title=params.title if params.title is not None else "",
            company_name=params.company_name if params.company_name is not None else "",
        )

        new_instance.save()
        return CreateCustomer(id=new_instance.id, ok=True, message='Customer created successfully')
