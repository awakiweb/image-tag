import graphene

from .models import Sale, SaleDetail, Invoice
from .types import SaleTypes, SaleDetailTypes, InvoiceTypes

from money.models import Money
from customer.models import Customer
from inventory.models import Inventory


# ************** INPUT MUTATIONS ************** #
# ************** #
class SaleDetailInput(graphene.InputObjectType):
    sale_id = graphene.Int(required=True)
    inventory_id = graphene.Int(required=True)

    price = graphene.Float(required=True)
    quantity = graphene.Float(required=True)
    active = graphene.Boolean(required=True)


class SaleInput(graphene.InputObjectType):
    money_id = graphene.Int(required=True)
    customer_id = graphene.Int()

    type = graphene.String(required=True)
    sale_date = graphene.DateTime(required=True)
    status = graphene.Int(required=True)

    sale_details = graphene.List(SaleDetailInput)


class InvoiceInput(graphene.InputObjectType):
    sale_id = graphene.Int(required=True)
    money_id = graphene.Int(required=True)

    type = graphene.String(required=True)
    amount = graphene.Float(required=True)

    invoice_date = graphene.DateTime(required=True)
    status = graphene.Int(required=True)


# ************** MUTATIONS ************** #
# ************** #
class CreateSale(graphene.Mutation):
    class Arguments:
        params = SaleInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()
    sale = graphene.Field(SaleTypes)

    def mutate(self, info, params):
        if params is None:
            return CreateSale(ok=False, message='Params were not provided', sale=None)

        money = Money.objects.get(pk=params.money_id)
        customer = Customer.objects.get(pk=params.customer_id) if params.customer_id != 0 else None

        if money is None:
            return CreateSale(ok=False, message='Money was not provided', sale=None)

        sale_instance = Sale(
            money=money,
            customer=customer,
            type=params.type,
            sale_date=params.sale_date,
            status=params.status
        )

        sale_instance.save()

        # save details
        if params.sale_details is None:
            return CreateSale(ok=True, message='Sale Saved Correctly', sale=sale_instance)

        for sale_detail in params.sale_details:
            inventory = Inventory.objects.get(pk=sale_detail.inventory_id)

            # if inventory exists, add new sale detail
            if inventory is not None:
                new_sale_detail = SaleDetail(
                    sale=sale_instance,
                    inventory=inventory,
                    price=sale_detail.price,
                    quantity=sale_detail.quantity,
                    active=sale_detail.active
                )

                new_sale_detail.save()

        return CreateSale(ok=True, message='Sale Saved Correctly', sale=sale_instance)


class CreateInvoice(graphene.Mutation):
    class Arguments:
        params = InvoiceInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()
    invoice = graphene.Field(InvoiceTypes)

    def mutate(self, info, params):
        if params is None:
            return CreateInvoice(ok=False, message='Params were not provided', invoice=None)

        sale = Sale.objects.get(pk=params.sale_id)
        money = Money.objects.get(pk=params.money_id)

        if sale is None:
            return CreateInvoice(ok=False, message='Sale was not provided', invoice=None)

        if money is None:
            return CreateInvoice(ok=False, message='Money was not provided', invoice=None)

        invoice_instance = Invoice(
            sale=sale,
            money=money,
            type=params.type,
            amount=params.amount,
            invoice_date=params.invoice_date,
            status=params.status
        )

        invoice_instance.save()
        return CreateInvoice(ok=True, message='Sale Saved Correctly', invoice=invoice_instance)


class UpdateSale(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)
        params = SaleInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()
    sale_detail = graphene.Field(SaleTypes)

    def mutate(self, info, identify, params=None):
        sale_instance = Sale.objects.get(pk=identify)

        if params is None:
            return UpdateSale(ok=False, message='Params were not provided', sale=None)

        money = Money.objects.get(pk=params.money_id)
        customer = Customer.objects.get(pk=params.customer_id) if params.customer_id != 0 else None

        if money is None:
            return CreateSale(ok=False, message='Money was not provided', sale=None)

        sale_instance.money = money
        sale_instance.customer = customer
        sale_instance.type = params.type if params.type else sale_instance.type
        sale_instance.status = params.status if params.status else sale_instance.status
        sale_instance.sale_date = params.sale_date if params.sale_date else sale_instance.sale_date

        sale_instance.save()

        return UpdateSale(ok=True, message='Sale Saved Correctly', sale=sale_instance)


class UpdateSaleDetail(graphene.Mutation):
    class Arguments:
        params = graphene.List(SaleDetailInput)

    ok = graphene.Boolean()
    message = graphene.String()
    sale_detail = graphene.List(SaleDetailTypes)

    def mutate(self, info, params):
        if params is None:
            return UpdateSaleDetail(ok=False, message='Params were not provided', sale_detail=None)

        new_sale_detail = []
        for param in params:
            # if sale_detail_id equals 0: create sale_detail
            try:
                sale_detail = SaleDetail.objects.get(sale_id=param.sale_id, inventory_id=param.inventory_id)

                sale_detail.price = param.price
                sale_detail.quantity = param.quantity
                sale_detail.active = param.active

                sale_detail.save()
                new_sale_detail.append(sale_detail)
            except SaleDetail.DoesNotExist:
                sale = Sale.objects.get(pk=param.sale_id)
                inventory = Inventory.objects.get(pk=param.inventory_id)

                if sale is None:
                    return UpdateSaleDetail(ok=False, message='Sale was not provided', sale_detail=None)

                if inventory is None:
                    return UpdateSaleDetail(ok=False, message='Product was not provided', sale_detail=None)

                sale_detail_instance = SaleDetail(
                    sale=sale,
                    inventory=inventory,
                    price=param.price,
                    quantity=param.quantity,
                    active=param.active
                )

                sale_detail_instance.save()
                new_sale_detail.append(sale_detail_instance)
        return UpdateSaleDetail(ok=True, message='Sale Detail Saved Correctly', sale_detail=new_sale_detail)
