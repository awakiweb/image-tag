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

        # find customer by email and last name
        existing_customer = Customer.objects.get(email=params.email, last_name=params.last_name)

        # if customer exists
        if existing_customer is not None:
            return CreateCustomer(id=existing_customer.id, ok=True, message='Customer created successfully')

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


class UpdateCustomer(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)
        params = CustomerInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, pk, params):
        if not pk:
            return UpdateCustomer(ok=False, message='Params are invalid')
        if not params:
            return UpdateCustomer(ok=False, message='Params are invalid')

        instance = Customer.objects.get(pk=pk)
        if instance:
            instance.first_name = params.first_name
            instance.last_name = params.last_name
            instance.email = params.email
            instance.phone_number = params.phone_number
            instance.title = params.title if params.title is not None else ""
            instance.company_name = params.company_name if params.company_name is not None else ""

            instance.save()
            return UpdateCustomer(ok=True, message='Customer updated successfully')
        return UpdateCustomer(ok=False, message='Customer was not updated')
