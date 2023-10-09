import graphene
from graphene_django.types import DjangoObjectType
from .models import Resource


class ResourceType(DjangoObjectType):
    county_url = graphene.String()
    city_url = graphene.String()

    class Meta:
        model = Resource

    def resolve_county_url(self, info):
        return info.context.build_absolute_uri(self.county_file_url())

    def resolve_city_url(self, info):
        return info.context.build_absolute_uri(self.city_file_url())
