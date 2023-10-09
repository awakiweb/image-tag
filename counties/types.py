from graphene_django.types import DjangoObjectType
from .models import County


class CountyType(DjangoObjectType):
    class Meta:
        model = County
