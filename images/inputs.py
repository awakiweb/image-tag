import graphene


class ImageInput(graphene.InputObjectType):
    url = graphene.String(required=True)
    tags = graphene.List(graphene.NonNull(graphene.String))
