from graphene_django.types import DjangoObjectType

from .models import Category


# ************** TYPES MODELS ************** #
# ************** #
class CategoryTypes(DjangoObjectType):
    class Meta:
        model = Category
