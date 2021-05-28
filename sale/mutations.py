import graphene

from .models import Sale, SaleDetail, Invoice
from .types import SaleTypes, SaleDetailTypes, InvoiceTypes

from money.models import Money
from product.models import Product
from customer.models import Customer


# ************** INPUT MUTATIONS ************** #
# ************** #
class SaleInput(graphene):
    money_id = graphene.Int(required=True)
    customer_id = graphene.Int(required=True)

    type = graphene.String(required=True)
    sale_date = graphene.DateTime(required=True)
    status = graphene.Int(required=True)


class SaleDetailInput(graphene):
    sale_id = graphene.Int(required=True)
    product_id = graphene.Int(required=True)

    price = graphene.Float(required=True)
    quantity = graphene.Float(required=True)
    active = graphene.Boolean(required=True)


class InvoiceInput(graphene):
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
        return CreateSale(ok=True, message='Sale Saved Correctly', sale=sale_instance)


class CreateSaleDetail(graphene.Mutation):
    class Arguments:
        params = SaleDetailInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()
    sale_detail = graphene.Field(SaleDetailTypes)

    def mutate(self, info, params):
        if params is None:
            return CreateSaleDetail(ok=False, message='Params were not provided', sale_detail=None)

        sale = Sale.objects.get(pk=params.sale_id)
        product = Product.objects.get(pk=params.product_id)

        if sale is None:
            return CreateSaleDetail(ok=False, message='Sale was not provided', sale_detail=None)

        if product is None:
            return CreateSaleDetail(ok=False, message='Product was not provided', sale_detail=None)

        sale_detail_instance = SaleDetail(
            sale=sale,
            product=product,
            price=params.price,
            quantity=params.quantity,
            active=params.active
        )

        sale_detail_instance.save()
        return CreateSaleDetail(ok=True, message='Sale Detail Saved Correctly', sale_detail=sale_detail_instance)


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
