import graphene
from graphene_django.types import ObjectType

from graphql_jwt.decorators import login_required

from images.models import Image, Tag
from images.types import ImageType, TagType


# ************** QUERY MODELS ************** #
# ************** #
class Query(ObjectType):
    images = graphene.List(ImageType)
    tags = graphene.List(TagType)

    images_by_tag = graphene.List(ImageType, tag=graphene.String())

    def resolve_images(self, info, **kwargs):
        return Image.objects.all()

    def resolve_tags(self, info, **kwargs):
        return Tag.objects.all()

    def resolve_images_by_tag(self, info, tag):
        return Image.objects.filter(image_tags__tag__name__icontains=tag)
