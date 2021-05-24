import graphene

from .models import Unit, Color
from .types import UnitTypes, ColorTypes


# ************** INPUT MUTATIONS ************** #
# ************** #
class UnitInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    symbol = graphene.String(required=True)
    description = graphene.String()

    active = graphene.Boolean()


class ColorInput(graphene.InputObjectType):
    code = graphene.String(required=True)
    name = graphene.String(required=True)
    description = graphene.String()

    active = graphene.Boolean()


# ************** MUTATIONS ************** #
# ************** #
class CreateUnit(graphene.Mutation):
    class Arguments:
        params = UnitInput(required=True)

    ok = graphene.Boolean()
    unit = graphene.Field(UnitTypes)

    def mutate(self, info, params):
        if params:
            unit_instance = Unit(
                name=params.name,
                symbol=params.symbol,
                description=params.description,
                active=True
            )

            unit_instance.save()
            return CreateUnit(ok=True, unit=unit_instance)
        return CreateUnit(ok=False, unit=None)


class UpdateUnit(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)
        params = UnitInput(required=True)

    ok = graphene.Boolean()
    unit = graphene.Field(UnitTypes)

    def mutate(self, info, identify, params=None):
        unit_instance = Unit.objects.get(pk=identify)

        if unit_instance:
            unit_instance.name = params.name if params.name else unit_instance.name
            unit_instance.symbol = params.symbol if params.symbol else unit_instance.symbol
            unit_instance.description = params.description if params.description else unit_instance.description
            unit_instance.active = params.active if params.active else unit_instance.active

            unit_instance.save()
            return UpdateUnit(ok=True, unit=unit_instance)
        return UpdateUnit(ok=False, unit=None)


class CreateColor(graphene.Mutation):
    class Arguments:
        params = ColorInput(required=True)

    ok = graphene.Boolean()
    color = graphene.Field(ColorTypes)

    def mutate(self, info, params):
        if params:
            color_instance = Color(
                code=params.code,
                name=params.name,
                description=params.description,
                active=True
            )

            color_instance.save()
            return CreateColor(ok=True, color=color_instance)
        return CreateColor(ok=False, color=None)


class UpdateColor(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)
        params = ColorInput(required=True)

    ok = graphene.Boolean()
    color = graphene.Field(ColorTypes)

    def mutate(self, info, identify, params=None):
        color_instance = Color.objects.get(pk=identify)

        if color_instance:
            color_instance.code = params.code if params.code else color_instance.code
            color_instance.name = params.name if params.name else color_instance.name
            color_instance.description = params.description if params.description else color_instance.description
            color_instance.active = params.active if params.active else color_instance.active

            color_instance.save()
            return UpdateColor(ok=True, color=color_instance)
        return UpdateColor(ok=False, color=None)

