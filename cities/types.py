from graphene_django.types import DjangoObjectType
from .models import City


class CityType(DjangoObjectType):
    class Meta:
        model = City
