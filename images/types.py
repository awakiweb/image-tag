import graphene
from graphene_django.types import DjangoObjectType
from .models import Image, Tag


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class ImageType(DjangoObjectType):
    tags = graphene.List(TagType)

    class Meta:
        model = Image

    def resolve_tags(self, info):
        return self.get_tags()
