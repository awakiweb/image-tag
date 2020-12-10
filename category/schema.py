import graphene
from graphene_django.types import DjangoObjectType

from .models import Category


# ************** TYPES MODELS ************** #
# ************** #
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


# ************** INPUT MUTATIONS ************** #
# ************** #
class CategoryInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String()

    level = graphene.Int()
    parent = graphene.Int()

    thumb = graphene.String()
    image = graphene.String()

    order = graphene.Int()
    active = graphene.Boolean()


# ************** MUTATIONS ************** #
# ************** #
class CreateCategory(graphene.Mutation):
    class Arguments:
        params = CategoryInput(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, params):
        if params:
            category_instance = Category(
                name=params.name,
                description=params.description,
                level=params.level,
                parent=params.parent,
                thumb=params.thumb,
                image=params.image,
                order=params.order,
                active=True
            )

            category_instance.save()
            return CreateCategory(ok=True, category=category_instance)
        return CreateCategory(ok=False, category=None)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)
        params = CategoryInput(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, identify, params=None):
        category_instance = Category.objects.get(pk=identify)

        if category_instance:
            category_instance.name = params.name if params.name else category_instance.name
            category_instance.description = params.description if params.description else category_instance.description
            category_instance.level = params.level if params.level else category_instance.level
            category_instance.parent = params.parent if params.parent else category_instance.parent
            category_instance.thumb = params.thumb if params.thumb else category_instance.thumb
            category_instance.image = params.image if params.image else category_instance.image
            category_instance.order = params.order if params.order else category_instance.order
            category_instance.active = params.active if params.active else category_instance.active

            category_instance.save()
            return UpdateCategory(ok=True, category=category_instance)
        return UpdateCategory(ok=False, category=None)

