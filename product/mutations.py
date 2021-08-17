import graphene
from django.db import transaction
from graphql_jwt.decorators import login_required

from .models import Brand, Model, Size, Product, ProductPrice
from .types import BrandTypes, ModelTypes, SizeTypes, ProductTypes

from category.models import Category
from money.models import Money


# ************** INPUT MUTATIONS ************** #
# ************** #
class BrandInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String()

    active = graphene.Boolean()


class ModelInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String()

    active = graphene.Boolean()


class SizeInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    active = graphene.Boolean()


class ProductInput(graphene.InputObjectType):
    size_id = graphene.Int(required=True)
    brand_id = graphene.Int(required=True)
    model_id = graphene.Int(required=True)
    category_id = graphene.Int(required=True)

    name = graphene.String(required=True)
    description = graphene.String()

    thumb = graphene.String()
    image = graphene.String()

    # not required
    purchase_price = graphene.Float()
    purchase_money_id = graphene.Int()

    # not required
    sale_price = graphene.Float()
    sale_money_id = graphene.Int()

    active = graphene.Boolean()


# ************** MUTATIONS ************** #
# ************** #
class CreateBrand(graphene.Mutation):
    class Arguments:
        params = BrandInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()
    brand = graphene.Field(BrandTypes)

    @login_required
    def mutate(self, info, params):
        if params is None:
            return CreateBrand(ok=False, message='Params were not provided', brand=None)

        try:
            exists = Brand.objects.get(name=params.name)

            if exists is not None:
                return CreateBrand(ok=False, message='Name already exists', brand=None)
        except Brand.DoesNotExist:
            brand_instance = Brand(
                name=params.name,
                description=params.description,
                active=True
            )

            brand_instance.save()
            return CreateBrand(ok=True, brand=brand_instance)


class UpdateBrand(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)
        params = BrandInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()
    brand = graphene.Field(BrandTypes)

    @login_required
    def mutate(self, info, identify, params=None):
        brand_instance = Brand.objects.get(pk=identify)

        if brand_instance is None:
            return UpdateBrand(ok=False, message='Brand does not exists', brand=None)

        if params is None:
            return UpdateBrand(ok=False, message='Params were not provided', brand=None)

        try:
            exists = Brand.objects.exclude(pk=identify).get(name=params.name)

            if exists is not None:
                return UpdateBrand(ok=False, message='Name already exists', brand=None)
        except Brand.DoesNotExist:
            brand_instance.name = params.name if params.name else brand_instance.name
            brand_instance.description = params.description if params.description else brand_instance.description
            brand_instance.active = params.active if params.active else brand_instance.active

            brand_instance.save()
            return UpdateBrand(ok=True, brand=brand_instance)


class CreateModel(graphene.Mutation):
    class Arguments:
        params = ModelInput(required=True)

    ok = graphene.Boolean()
    model = graphene.Field(ModelTypes)

    @login_required
    def mutate(self, info, params):
        if params:
            model_instance = Model(
                name=params.name,
                description=params.description,
                active=True
            )

            model_instance.save()
            return CreateModel(ok=True, model=model_instance)
        return CreateModel(ok=False, model=None)


class UpdateModel(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)
        params = ModelInput(required=True)

    ok = graphene.Boolean()
    model = graphene.Field(ModelTypes)

    @login_required
    def mutate(self, info, identify, params=None):
        model_instance = Model.objects.get(pk=identify)

        if model_instance:
            model_instance.name = params.name if params.name else model_instance.name
            model_instance.description = params.description if params.description else model_instance.description
            model_instance.active = params.active if params.active else model_instance.active

            model_instance.save()
            return UpdateModel(ok=True, model=model_instance)
        return UpdateModel(ok=False, model=None)


class CreateSize(graphene.Mutation):
    class Arguments:
        params = SizeInput(required=True)

    ok = graphene.Boolean()
    size = graphene.Field(SizeTypes)

    @login_required
    def mutate(self, info, params):
        if params:
            size_instance = Size(
                name=params.name,
                active=True
            )

            size_instance.save()
            return CreateSize(ok=True, size=size_instance)
        return CreateSize(ok=False, size=None)


class UpdateSize(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)
        params = SizeInput(required=True)

    ok = graphene.Boolean()
    size = graphene.Field(SizeTypes)

    @login_required
    def mutate(self, info, identify, params=None):
        size_instance = Size.objects.get(pk=identify)

        if size_instance:
            size_instance.name = params.name if params.name else size_instance.name
            size_instance.active = params.active if params.active else size_instance.active

            size_instance.save()
            return UpdateSize(ok=True, size=size_instance)
        return UpdateSize(ok=False, size=None)


class CreateProduct(graphene.Mutation):
    class Arguments:
        params = ProductInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()
    product = graphene.Field(ProductTypes)

    @login_required
    @transaction.atomic()
    def mutate(self, info, params):
        if params is None:
            return CreateProduct(ok=False, message='LOS PARAMETROS DEL PRODUCTOS NO ESTAN DEFINIDOS', product=None)

        if params.purchase_price is None:
            return CreateProduct(ok=False, message='EL PRECIO DE COMPRA NO FUE DEFINIDO', product=None)

        if params.sale_price is None:
            return CreateProduct(ok=False, message='EL PECIO DE VENTA NO FUE DEFINIDO', product=None)

        size = Size.objects.get(pk=params.size_id)
        brand = Brand.objects.get(pk=params.brand_id)
        model = Model.objects.get(pk=params.model_id)
        category = Category.objects.get(pk=params.category_id)

        if size is None:
            return CreateProduct(ok=False, message='EL TAMANO NO FUE DEFINIDO', product=None)

        if brand is None:
            return CreateProduct(ok=False, message='LA MARCA NO FUE DEFINIDA', product=None)

        if model is None:
            return CreateProduct(ok=False, message='EL MODELO NO FUE DEFINIDO', product=None)

        if category is None:
            return CreateProduct(ok=False, message='LA CATEGORIA NO FUE DEFINIDA', product=None)

        product_instance = Product(
            size=size,
            brand=brand,
            model=model,
            category=category,
            name=params.name,
            description=params.description,
            thumb=params.thumb,
            image=params.image,
            active=True
        )

        # after save product, save prices
        product_instance.save()

        if product_instance.pk is None:
            return CreateProduct(ok=False, message='EL PRODUCTO NO FUE GUARDADO, INTENTE MAS TARDE', product=None)

        # SAVE PURCHASE PRICE IF EXISTS
        if params.purchase_price:
            purchase_money = Money.objects.get(pk=params.purchase_money_id)

            if purchase_money is not None:
                purchase = ProductPrice(
                    product=product_instance,
                    money=purchase_money,
                    price_type=ProductPrice.PURCHASE_PRICE,
                    price=params.purchase_price,
                    active=True
                )

                purchase.save()

        # SAVE SALE PRICE IF EXISTS
        if params.sale_price:
            sale_money = Money.objects.get(pk=params.sale_money_id)

            if sale_money is not None:
                sale = ProductPrice(
                    product=product_instance,
                    money=sale_money,
                    price_type=ProductPrice.SALE_PRICE,
                    price=params.sale_price,
                    active=True
                )

                sale.save()

        return CreateProduct(ok=True, message='', product=product_instance)


class UpdateProduct(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)
        params = ProductInput(required=True)

    ok = graphene.Boolean()
    product = graphene.Field(ProductTypes)

    @login_required
    @transaction.atomic()
    def mutate(self, info, identify, params=None):
        product_instance = Product.objects.get(pk=identify)

        if product_instance is None:
            return UpdateProduct(ok=False, product=None)

        if params is None:
            return CreateProduct(ok=False, product=None)

        if params.purchase_price is None:
            return CreateProduct(ok=False, product=None)

        if params.sale_price is None:
            return CreateProduct(ok=False, product=None)

        size = Size.objects.get(pk=params.size_id)
        brand = Brand.objects.get(pk=params.brand_id)
        model = Model.objects.get(pk=params.model_id)
        category = Category.objects.get(pk=params.category_id)

        if size is None:
            size = product_instance.size

        if brand is None:
            brand = product_instance.brand

        if model is None:
            model = product_instance.model

        if category is None:
            category = product_instance.category

        product_instance.size = size
        product_instance.brand = brand
        product_instance.model = model
        product_instance.category = category
        product_instance.name = params.name if params.name else product_instance.name
        product_instance.description = params.description if params.description else product_instance.description
        product_instance.thumb = params.thumb if params.thumb else product_instance.thumb
        product_instance.image = params.image if params.image else product_instance.image
        product_instance.active = params.active if params.active else product_instance.active

        # after update product, verify if prices had changes
        product_instance.save()

        purchase = ProductPrice.objects.get(
            product=product_instance, active=True, price_type=ProductPrice.PURCHASE_PRICE)
        sale = ProductPrice.objects.get(
            product=product_instance, active=True, price_type=ProductPrice.SALE_PRICE)

        purchase_money = Money.objects.get(pk=params.purchase_money_id)
        sale_money = Money.objects.get(pk=params.sale_money_id)

        # if new purchase price is different from preview one
        # create new purchase price and made last price un active
        if purchase.price != params.purchase_price:
            purchase.active = False
            purchase.save()

            new_purchase = ProductPrice(
                product=product_instance,
                money=purchase_money,
                price_type=ProductPrice.PURCHASE_PRICE,
                price=params.purchase_price,
                active=True
            )

            new_purchase.save()
        elif purchase.price == params.purchase_price:
            # if the price is the same but money it is different
            # modify only money
            if purchase.money.id != purchase_money.id:
                purchase.money = purchase_money
                purchase.save()

        # if new sale price is different from preview one
        # create new sale price and made last price un active
        if sale.price != params.sale_price:
            sale.active = False
            sale.save()

            new_sale = ProductPrice(
                product=product_instance,
                price_type=ProductPrice.SALE_PRICE,
                price=params.sale_price,
                money=sale_money,
                active=True
            )

            new_sale.save()
        elif sale.price == params.sale_price:
            # if the price is the same but money it is different
            # modify only money
            if sale.money.id != sale_money.id:
                sale.money = sale_money
                sale.save()

        return UpdateProduct(ok=True, product=product_instance)
