import graphene
from graphql_jwt.decorators import login_required

from .models import Category
from .types import CategoryTypes


# ************** INPUT MUTATIONS ************** #
# ************** #
class CategoryInput(graphene.InputObjectType):
    code = graphene.String(required=True)
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

    ok = graphene.Boolean()
    category = graphene.Field(CategoryTypes)

    @login_required
    def mutate(self, info, params):
        if params is None:
            return CreateCategory(ok=False, category=None)

        if params.parent == 0:
            parent = None
        else:
            parent = Category.objects.get(pk=params.parent)

        category_instance = Category(
            code=params.code,
            name=params.name,
            description=params.description,
            level=params.level,
            parent=parent,
            thumb=params.thumb,
            image=params.image,
            order=params.order,
            active=True
        )

        category_instance.save()
        return CreateCategory(ok=True, category=category_instance)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)
        params = CategoryInput(required=True)

    ok = graphene.Boolean()
    category = graphene.Field(CategoryTypes)

    @login_required
    def mutate(self, info, identify, params=None):
        category_instance = Category.objects.get(pk=identify)

        if category_instance is None:
            return UpdateCategory(ok=False, category=None)

        if params is None:
            return UpdateCategory(ok=False, category=None)

        if params.parent == 0:
            parent = None
        else:
            parent = Category.objects.get(pk=params.parent)

        category_instance.code = params.code if params.code else category_instance.code
        category_instance.name = params.name if params.name else category_instance.name
        category_instance.description = params.description if params.description else category_instance.description
        category_instance.level = params.level if params.level else category_instance.level
        category_instance.parent = parent if params.parent else category_instance.parent
        category_instance.thumb = params.thumb if params.thumb else category_instance.thumb
        category_instance.image = params.image if params.image else category_instance.image
        category_instance.order = params.order if params.order else category_instance.order
        category_instance.active = params.active if params.active else category_instance.active

        category_instance.save()
        return UpdateCategory(ok=True, category=category_instance)
