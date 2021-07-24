import graphene
from graphql_jwt.decorators import login_required

from .models import Customer
from .types import CustomerTypes


# ************** INPUT MUTATIONS ************** #
# ************** #
class CustomerInput(graphene.InputObjectType):
    identification = graphene.String(required=True)
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)

    genre = graphene.String()
    email = graphene.String()
    address = graphene.String()
    phone_number = graphene.String()

    active = graphene.Boolean()


# ************** MUTATIONS ************** #
# ************** #
class CreateCustomer(graphene.Mutation):
    class Arguments:
        params = CustomerInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()
    customer = graphene.Field(CustomerTypes)

    @login_required
    def mutate(self, info, params):
        if params is None:
            return CreateCustomer(ok=False, message='Params were not provided', customer=None)

        if params.genre is not Customer.MALE and params.genre is not Customer.FEMALE:
            return CreateCustomer(ok=False, message='Genre value has to be M or F', customer=None)

        try:
            exists = Customer.objects.get(identification=params.identification)

            if exists is not None:
                return CreateCustomer(ok=False, message='Identification already exists', customer=None)
        except Customer.DoesNotExist:
            customer_instance = Customer(
                identification=params.identification,
                first_name=params.first_name,
                last_name=params.last_name,
                genre=params.genre,
                email=params.email,
                address=params.address,
                phone_number=params.phone_number,
                active=True
            )

            customer_instance.save()
            return CreateCustomer(ok=True, customer=customer_instance)


class UpdateCustomer(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)
        params = CustomerInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()
    customer = graphene.Field(CustomerTypes)

    @login_required
    def mutate(self, info, identify, params=None):
        customer_instance = Customer.objects.get(pk=identify)

        if customer_instance is None:
            return UpdateCustomer(ok=False, message='Customer does not exists', customer=None)

        if params is None:
            return UpdateCustomer(ok=False, message='Params were not provided', customer=None)

        if params.genre is not Customer.MALE and params.genre is not Customer.FEMALE:
            return CreateCustomer(ok=False, message='Genre value has to be M or F', customer=None)

        try:
            exists = Customer.objects.exclude(pk=identify).get(identification=params.identification)

            if exists is not None:
                return UpdateCustomer(ok=False, message='Identification already exists', customer=None)
        except Customer.DoesNotExist:
            customer_instance.identification = params.identification if params.identification else customer_instance.identification
            customer_instance.first_name = params.first_name if params.first_name else customer_instance.first_name
            customer_instance.last_name = params.last_name if params.last_name else customer_instance.last_name
            customer_instance.genre = params.genre if params.genre else customer_instance.genre
            customer_instance.email = params.email if params.email else customer_instance.email
            customer_instance.address = params.address if params.address else customer_instance.address
            customer_instance.phone_number = params.phone_number if params.phone_number else customer_instance.phone_number
            customer_instance.active = params.active if params.active else customer_instance.active

            customer_instance.save()
            return UpdateCustomer(ok=True, customer=customer_instance)
