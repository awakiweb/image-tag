import graphene
from graphene_django.types import ObjectType

from money.models import Money, ExchangeRate
from money.types import MoneyTypes, ExchangeRateTypes

from category.models import Category
from category.types import CategoryTypes

from product.models import Brand, Model, Size, Product
from product.types import BrandTypes, ModelTypes, SizeTypes, ProductTypes

from product_detail.models import Unit, Color
from product_detail.types import UnitTypes, ColorTypes

from inventory.models import Store, Inventory, MovementType, Movement
from inventory.types import StoreTypes, InventoryTypes, MovementTypeTypes, MovementTypes

from customer.models import Customer
from customer.types import CustomerTypes

from sale.models import Sale, SaleDetail, Invoice
from sale.types import SaleTypes, SaleDetailTypes, InvoiceTypes


# ************** QUERY MODELS ************** #
# ************** #
class Query(ObjectType):
    # ************** MONEYS ************** #
    # ************** #
    not_principal_money = graphene.List(MoneyTypes)
    principal_money = graphene.Field(MoneyTypes)
    money = graphene.Field(MoneyTypes, id=graphene.Int())
    moneys = graphene.List(MoneyTypes)

    exchange_rate = graphene.Field(ExchangeRateTypes, id=graphene.Int())
    exchange_rates = graphene.List(ExchangeRateTypes)

    # ************** CATEGORIES ************** #
    # ************** #
    category = graphene.Field(CategoryTypes, id=graphene.Int())
    categories = graphene.List(CategoryTypes)

    # ************** PRODUCTS ************** #
    # ************** #
    brand = graphene.Field(BrandTypes, id=graphene.Int())
    brands = graphene.List(BrandTypes)

    model = graphene.Field(ModelTypes, id=graphene.Int())
    models = graphene.List(ModelTypes)

    size = graphene.Field(SizeTypes, id=graphene.Int())
    sizes = graphene.List(SizeTypes)

    product = graphene.Field(ProductTypes, id=graphene.Int())
    products = graphene.List(ProductTypes)

    # ************** PRODUCT DETAILS ************** #
    # ************** #
    unit = graphene.Field(UnitTypes, id=graphene.Int())
    units = graphene.List(UnitTypes)

    color = graphene.Field(ColorTypes, id=graphene.Int())
    colors = graphene.List(ColorTypes)

    # ************** INVENTORIES ************** #
    # ************** #
    store = graphene.Field(StoreTypes, id=graphene.Int())
    stores = graphene.List(StoreTypes)

    inventory = graphene.Field(InventoryTypes, id=graphene.Int())
    inventories = graphene.List(InventoryTypes)

    movement_type = graphene.Field(MovementTypeTypes, id=graphene.Int())
    movement_types = graphene.List(MovementTypeTypes)

    movement = graphene.Field(MovementTypes, id=graphene.Int())
    movements = graphene.List(MovementTypes)

    # ************** CUSTOMERS ************** #
    # ************** #
    customer = graphene.Field(CustomerTypes, id=graphene.Int())
    customers = graphene.List(CustomerTypes)

    # ************** SALES ************** #
    # ************** #
    sale = graphene.Field(SaleTypes, id=graphene.Int())
    sales = graphene.List(SaleTypes)

    sale_detail = graphene.Field(SaleDetailTypes, id=graphene.Int())
    sale_details = graphene.List(SaleDetailTypes)

    invoice = graphene.Field(InvoiceTypes, id=graphene.Int())
    invoices = graphene.List(InvoiceTypes)

    # ************** MONEYS ************** #
    # ************** #
    def resolve_not_principal_money(self, info, **kwargs):
        return Money.objects.filter(principal=False)

    def resolve_principal_money(self, info, **kwargs):
        return Money.objects.get(principal=True)

    def resolve_money(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Money.objects.get(pk=identity)

        return None

    def resolve_moneys(self, info, **kwargs):
        return Money.objects.all()

    def resolve_exchange_rate(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return ExchangeRate.objects.get(pk=identity)

        return None

    def resolve_exchange_rates(self, info, **kwargs):
        return ExchangeRate.objects.all()

    # ************** CATEGORIES ************** #
    # ************** #
    def resolve_category(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Category.objects.get(pk=identity)

        return None

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()

    # ************** BRANDS ************** #
    # ************** #
    def resolve_brand(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Brand.objects.get(pk=identity)

        return None

    def resolve_brands(self, info, **kwargs):
        return Brand.objects.all()

    # ************** MODELS ************** #
    # ************** #
    def resolve_model(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Model.objects.get(pk=identity)

        return None

    def resolve_models(self, info, **kwargs):
        return Model.objects.all()

    # ************** SIZES ************** #
    # ************** #
    def resolve_size(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Size.objects.get(pk=identity)

        return None

    def resolve_sizes(self, info, **kwargs):
        return Size.objects.all()

    # ************** PRODUCTS ************** #
    # ************** #
    def resolve_product(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Product.objects.get(pk=identity)

        return None

    def resolve_products(self, info, **kwargs):
        return Product.objects.all()

    # ************** UNITS ************** #
    # ************** #
    def resolve_unit(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Unit.objects.get(pk=identity)

        return None

    def resolve_units(self, info, **kwargs):
        return Unit.objects.all()

    # ************** COLORS ************** #
    # ************** #
    def resolve_color(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Color.objects.get(pk=identity)

        return None

    def resolve_colors(self, info, **kwargs):
        return Color.objects.all()

    # ************** STORES ************** #
    # ************** #
    def resolve_store(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Store.objects.get(pk=identity)

        return None

    def resolve_stores(self, info, **kwargs):
        return Store.objects.all()

    # ************** INVENTORIES ************** #
    # ************** #
    def resolve_inventory(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Inventory.objects.get(pk=identity)

        return None

    def resolve_inventories(self, info, **kwargs):
        return Inventory.objects.all()

    # ************** MOVEMENT TYPES ************** #
    # ************** #
    def resolve_movement_type(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return MovementType.objects.get(pk=identity)

        return None

    def resolve_movement_types(self, info, **kwargs):
        return MovementType.objects.all()

    # ************** MOVEMENTS ************** #
    # ************** #
    def resolve_movement(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Movement.objects.get(pk=identity)

        return None

    def resolve_movements(self, info, **kwargs):
        return Movement.objects.all()

    # ************** CUSTOMERS ************** #
    # ************** #
    def resolve_customer(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Customer.objects.get(pk=identity)

        return None

    def resolve_customers(self, info, **kwargs):
        return Customer.objects.all()

    # ************** SALES ************** #
    # ************** #
    def resolve_sale(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Sale.objects.get(pk=identity)

        return None

    def resolve_sales(self, info, **kwargs):
        return Sale.objects.all()

    def resolve_sale_detail(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return SaleDetail.objects.get(pk=identity)

        return None

    def resolve_sale_details(self, info, **kwargs):
        return SaleDetail.objects.all()

    def resolve_invoice(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Invoice.objects.get(pk=identity)

        return None

    def resolve_invoices(self, info, **kwargs):
        return Invoice.objects.all()
