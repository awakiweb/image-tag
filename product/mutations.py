import graphene
from django.db import transaction

from .models import Brand, Model, Size, Product, ProductPrice
from .types import BrandTypes, ModelTypes, SizeTypes, ProductTypes

from category.models import Category


# ************** INPUT MUTATIONS ************** #
# ************** #
class BrandInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String()

    active = graphene.Boolean()


class ModelInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String()

    brand_id = graphene.Int(required=True)
    active = graphene.Boolean()


class SizeInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    active = graphene.Boolean()


class ProductInput(graphene.InputObjectType):
    size_id = graphene.Int(required=True)
    model_id = graphene.Int(required=True)
    category_id = graphene.Int(required=True)

    name = graphene.String(required=True)
    description = graphene.String()

    thumb = graphene.String()
    image = graphene.String()

    purchase_price = graphene.Float()
    sale_price = graphene.Float()

    active = graphene.Boolean()


# ************** MUTATIONS ************** #
# ************** #
class CreateBrand(graphene.Mutation):
    class Arguments:
        params = BrandInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()
    brand = graphene.Field(BrandTypes)

    def mutate(self, info, params):
        if params is None:
            return CreateBrand(ok=False, message='Params were nos provided', brand=None)

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

    def mutate(self, info, params):
        if params:
            brand = Brand.objects.get(pk=params.brand_id)

            if brand is None:
                return CreateModel(ok=False, model=None)

            model_instance = Model(
                name=params.name,
                brand=brand,
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

    def mutate(self, info, identify, params=None):
        model_instance = Model.objects.get(pk=identify)

        if model_instance:
            model_instance.name = params.name if params.name else model_instance.name
            model_instance.brand = params.brand_id if params.brand_id else model_instance.brand
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
    product = graphene.Field(ProductTypes)

    @transaction.atomic()
    def mutate(self, info, params):
        if params is None:
            return CreateProduct(ok=False, product=None)

        if params.purchase_price is None:
            return CreateProduct(ok=False, product=None)

        if params.sale_price is None:
            return CreateProduct(ok=False, product=None)

        size = Size.objects.get(pk=params.size_id)
        model = Model.objects.get(pk=params.model_id)
        category = Category.objects.get(pk=params.category_id)

        if size is None:
            return CreateProduct(ok=False, product=None)

        if model is None:
            return CreateProduct(ok=False, product=None)

        if category is None:
            return CreateProduct(ok=False, product=None)

        product_instance = Product(
            size=size,
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
            return CreateProduct(ok=False, product=None)

        purchase = ProductPrice(
            product=product_instance,
            price_type=ProductPrice.PURCHASE_PRICE,
            price=params.purchase_price,
            active=True
        )

        sale = ProductPrice(
            product=product_instance,
            price_type=ProductPrice.SALE_PRICE,
            price=params.sale_price,
            active=True
        )

        purchase.save()
        sale.save()

        return CreateProduct(ok=True, product=product_instance)


class UpdateProduct(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)
        params = ProductInput(required=True)

    ok = graphene.Boolean()
    product = graphene.Field(ProductTypes)

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
        model = Model.objects.get(pk=params.model_id)
        category = Category.objects.get(pk=params.category_id)

        if size is None:
            size = product_instance.size

        if model is None:
            model = product_instance.model

        if category is None:
            category = product_instance.category

        product_instance.size = size
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

        # if new purchase price is different from preview one
        # create new purchase price and made last price un active
        if purchase.price != params.purchase_price:
            purchase.active = False
            purchase.save()

            new_purchase = ProductPrice(
                product=product_instance,
                price_type=ProductPrice.PURCHASE_PRICE,
                price=params.purchase_price,
                active=True
            )

            new_purchase.save()

        # if new sale price is different from preview one
        # create new sale price and made last price un active
        if sale.price != params.sale_price:
            sale.active = False
            sale.save()

            new_sale = ProductPrice(
                product=product_instance,
                price_type=ProductPrice.SALE_PRICE,
                price=params.sale_price,
                active=True
            )

            new_sale.save()

        return UpdateProduct(ok=True, product=product_instance)