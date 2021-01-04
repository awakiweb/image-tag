import graphene
from graphene_django.types import ObjectType

from category.models import Category
from category.schema import CategoryType
from category.schema import CreateCategory, UpdateCategory

from product.models import Brand, Model, Size, Unit, Color, Product
from product.schema import BrandType, ModelType, SizeType, UnitType, ColorType, ProductType
from product.schema import CreateBrand, CreateModel, CreateSize, CreateUnit, CreateColor, CreateProduct
from product.schema import UpdateBrand, UpdateModel, UpdateSize, UpdateUnit, UpdateColor, UpdateProduct


# ************** QUERY MODELS ************** #
# ************** #
class Query(ObjectType):
    # ************** CATEGORIES ************** #
    # ************** #
    category = graphene.Field(CategoryType, id=graphene.Int())
    categories = graphene.List(CategoryType)

    # ************** PRODUCTS ************** #
    # ************** #
    brand = graphene.Field(BrandType, id=graphene.Int())
    brands = graphene.List(BrandType)

    model = graphene.Field(ModelType, id=graphene.Int())
    models = graphene.List(ModelType)

    size = graphene.Field(SizeType, id=graphene.Int())
    sizes = graphene.List(SizeType)

    unit = graphene.Field(UnitType, id=graphene.Int())
    units = graphene.List(UnitType)

    color = graphene.Field(ColorType, id=graphene.Int())
    colors = graphene.List(ColorType)

    product = graphene.Field(ProductType, id=graphene.Int())
    products = graphene.List(ProductType)

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

    # size
    def resolve_size(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Size.objects.get(pk=identity)

        return None

    def resolve_sizes(self, info, **kwargs):
        return Size.objects.all()

    # unit
    def resolve_unit(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Unit.objects.get(pk=identity)

        return None

    def resolve_units(self, info, **kwargs):
        return Unit.objects.all()

    # color
    def resolve_color(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Color.objects.get(pk=identity)

        return None

    def resolve_colors(self, info, **kwargs):
        return Color.objects.all()

    # product
    def resolve_product(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Product.objects.get(pk=identity)

        return None

    def resolve_products(self, info, **kwargs):
        return Product.objects.all()


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()

    create_brand = CreateBrand.Field()
    update_brand = UpdateBrand.Field()

    create_model = CreateModel.Field()
    update_model = UpdateModel.Field()

    create_size = CreateSize.Field()
    update_size = UpdateSize.Field()

    create_color = CreateColor.Field()
    update_color = UpdateColor.Field()

    create_unit = CreateUnit.Field()
    update_unit = UpdateUnit.Field()

    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
