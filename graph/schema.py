import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from product.models import Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class Query(ObjectType):
    category = graphene.Field(CategoryType, id=graphene.Int())
    categories = graphene.List(CategoryType)

    def resolve_category(self, info, **kwargs):
        identity = kwargs.get('id')

        if identity is not None:
            return Category.objects.get(pk=identity)

        return None

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()


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
