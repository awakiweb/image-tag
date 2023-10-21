import graphene
from django.core.exceptions import ObjectDoesNotExist

from .models import Image, Tag, ImageTag
from .inputs import ImageInput


class CreateImage(graphene.Mutation):
    class Arguments:
        params = ImageInput(required=True)

    id = graphene.Int()
    ok = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, params):
        if not params:
            return CreateImage(id=0, ok=False, message='Params are invalid')

        new_instance = Image(url=params.url)
        new_instance.save()

        # create tags
        if len(params.tags) > 0:
            # iterate tags
            for tag in params.tags:
                # check if tag exists
                try:
                    tag_exists = Tag.objects.get(name=tag)

                    image_tag = ImageTag(image=new_instance, tag=tag_exists)
                    image_tag.save()
                except ObjectDoesNotExist:
                    new_tag = Tag(name=tag)
                    new_tag.save()

                    image_tag = ImageTag(image=new_instance, tag=new_tag)
                    image_tag.save()

        return CreateImage(id=new_instance.id, ok=True, message='Image saved successfully')


class UpdateImage(graphene.Mutation):
    class Arguments:
        pk = graphene.Int()
        params = ImageInput(required=True)

    id = graphene.Int()
    ok = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, pk, params):
        if not params:
            return UpdateImage(id=0, ok=False, message='Params are invalid')

        image = Image.objects.get(pk=pk)
        image.url = params.url
        image.save()

        # delete all related tags
        image_tags = ImageTag.objects.filter(image=image)
        for image_tag in image_tags:
            image_tag.delete()

        # create tags
        if len(params.tags) > 0:
            # iterate tags
            for tag in params.tags:
                # check if tag exists
                try:
                    tag_exists = Tag.objects.get(name=tag)

                    image_tag = ImageTag(image=image, tag=tag_exists)
                    image_tag.save()
                except ObjectDoesNotExist:
                    new_tag = Tag(name=tag)
                    new_tag.save()

                    image_tag = ImageTag(image=image, tag=new_tag)
                    image_tag.save()

        return UpdateImage(id=image.id, ok=True, message='Image updated successfully')


class DeleteImage(graphene.Mutation):
    class Arguments:
        pk = graphene.Int()

    id = graphene.Int()
    ok = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, pk):
        image = Image.objects.get(pk=pk)

        # delete all related tags
        image_tags = ImageTag.objects.filter(image=image)
        for image_tag in image_tags:
            image_tag.delete()

        image.delete()
        return DeleteImage(id=pk, ok=True, message='Image deleted successfully')
