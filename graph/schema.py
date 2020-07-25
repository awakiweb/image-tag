import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from product.models import Category, Subcategory, Brand, Size, Unit, Color, Product, ProductPrice


## TYPES MODELS ##
# ************** #
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class SubcategoryType(DjangoObjectType):
    class Meta:
        model = Subcategory


class BrandType(DjangoObjectType):
    class Meta:
        model = Brand


class SizeType(DjangoObjectType):
    class Meta:
        model = Size


class UnitType(DjangoObjectType):
    class Meta:
        model = Unit


class ColorType(DjangoObjectType):
    class Meta:
        model = Color


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class ProductPriceType(DjangoObjectType):
    class Meta:
        model = ProductPrice


## QUERY MODELS ##
# ************** #
class Query(ObjectType):
    category = graphene.Field(CategoryType, id=graphene.Int())
    categories = graphene.List(CategoryType)

    subcategory = graphene.Field(SubcategoryType, id=graphene.Int())
    subcategories = graphene.List(SubcategoryType)

    brand = graphene.Field(BrandType, id=graphene.Int())
    brands = graphene.List(BrandType)

    size = graphene.Field(SizeType, id=graphene.Int())
    sizes = graphene.List(SizeType)

    unit = graphene.Field(UnitType, id=graphene.Int())
    units = graphene.List(UnitType)

    color = graphene.Field(ColorType, id=graphene.Int())
    colors = graphene.List(ColorType)

    product = graphene.Field(ProductType, id=graphene.Int())
    products = graphene.List(ProductType)

    productPrice = graphene.Field(ProductPriceType, id=graphene.Int())
    productPrices = graphene.List(ProductPriceType)

    # category
    def resolve_category(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Category.objects.get(pk=identity)

        return None

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()

    # subcategory
    def resolve_subcategory(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Subcategory.objects.get(pk=identity)

        return None

    def resolve_subcategories(self, info, **kwargs):
        return Subcategory.objects.all()

    # brand
    def resolve_brand(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Brand.objects.get(pk=identity)

        return None

    def resolve_brands(self, info, **kwargs):
        return Brand.objects.all()

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

    # product price
    def resolve_productPrice(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return ProductPrice.objects.get(pk=identity)

        return None

    def resolve_productPrices(self, info, **kwargs):
        return ProductPrice.objects.all()


class CategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()
    order = graphene.ID()


class CreateCategory(graphene.Mutation):
    class Arguments:
        input = CategoryInput(required=True)

    ok = graphene.Boolean()
    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True

        category_instance = Category(
            name=input.name,
            description=input.description,
            order=input.order
        )

        category_instance.save()
        return CreateCategory(ok=ok, category=category_instance)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = CategoryInput(required=True)

    ok = graphene.Boolean()
    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        category_instance = Category.objects.get(pk=id)

        if category_instance:
            ok = True
            category_instance.name = input.name
            category_instance.description = input.description
            category_instance.order = input.order

            category_instance.save()
            return UpdateCategory(ok=ok, category=category_instance)
        return UpdateCategory(ok=ok, category=None)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
