import graphene

from .models import Store, Inventory, MovementType, Movement
from .types import StoreTypes, InventoryTypes, MovementTypeTypes, MovementTypes

from product.models import Product


# ************** INPUT MUTATIONS ************** #
# ************** #
class StoreInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String()
    address = graphene.String()
    active = graphene.Boolean()


class InventoryInput(graphene.InputObjectType):
    store_id = graphene.Int(required=True)
    product_id = graphene.Int(required=True)

    available = graphene.Float()
    stock = graphene.Float()
    active = graphene.Boolean()


class MovementTypeInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    type = graphene.String(required=True)
    active = graphene.Boolean()


class MovementInput(graphene.InputObjectType):
    movement_type_id = graphene.Int(required=True)
    inventory_id = graphene.Int(required=True)

    date = graphene.DateTime(required=True)
    quantity = graphene.Float(required=True)
    description = graphene.String()
    active = graphene.Boolean()


# ************** MUTATIONS ************** #
# ************** #
class CreateStore(graphene.Mutation):
    class Arguments:
        params = StoreInput(required=True)

    ok = graphene.Boolean()
    store = graphene.Field(StoreTypes)

    def mutate(self, info, params):
        if params:
            store_instance = Store(
                name=params.name,
                description=params.description,
                address=params.address,
                active=True
            )

            store_instance.save()
            return CreateStore(ok=True, store=store_instance)
        return CreateStore(ok=False, store=None)


class UpdateStore(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)
        params = StoreInput(required=True)

    ok = graphene.Boolean()
    store = graphene.Field(StoreTypes)

    def mutate(self, info, identify, params=None):
        store_instance = Store.objects.get(pk=identify)

        if store_instance:
            store_instance.name = params.name if params.name else store_instance.name
            store_instance.description = params.description if params.description else store_instance.description
            store_instance.address = params.address if params.address else store_instance.address
            store_instance.active = params.active if params.active else store_instance.active

            store_instance.save()
            return UpdateStore(ok=True, store=store_instance)
        return UpdateStore(ok=False, store=None)


class CreateInventory(graphene.Mutation):
    class Arguments:
        params = InventoryInput(required=True)

    ok = graphene.Boolean()
    inventory = graphene.Field(InventoryTypes)

    def mutate(self, info, params):
        if params is None:
            return CreateInventory(ok=False, inventory=None)

        store = Store.objects.get(pk=params.store_id)
        product = Product.objects.get(pk=params.product_id)

        if store is None:
            return CreateInventory(ok=False, inventory=None)

        if product is None:
            return CreateInventory(ok=False, inventory=None)

        inventory_instance = Inventory(
            store=store,
            product=product,
            available=params.available,
            stock=params.stock,
            active=True
        )

        inventory_instance.save()
        return CreateInventory(ok=True, inventory=inventory_instance)


class UpdateInventory(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)
        params = InventoryInput(required=True)

    ok = graphene.Boolean()
    inventory = graphene.Field(InventoryTypes)

    def mutate(self, info, identify, params=None):
        inventory_instance = Inventory.objects.get(pk=identify)

        if inventory_instance is None:
            return UpdateInventory(ok=False, inventory=None)

        if params is None:
            return UpdateInventory(ok=False, inventory=None)

        store = Store.objects.get(pk=params.store_id)
        product = Product.objects.get(pk=params.product_id)

        if store is None:
            store = inventory_instance.store

        if product is None:
            product = inventory_instance.product

        inventory_instance.store = store
        inventory_instance.product = product
        inventory_instance.available = params.available if params.available else inventory_instance.available
        inventory_instance.stock = params.stock if params.stock else inventory_instance.stock
        inventory_instance.active = params.active if params.active else inventory_instance.active

        inventory_instance.save()
        return UpdateInventory(ok=True, inventory=inventory_instance)


class CreateMovementType(graphene.Mutation):
    class Arguments:
        params = MovementTypeInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()
    movementType = graphene.Field(MovementTypeTypes)

    def mutate(self, info, params):
        if params is None:
            return CreateMovementType(ok=False, message='Params is not defined', movementType=None)

        if params.type is not MovementType.ENTRY and params.type is not MovementType.DEPARTURE:
            return CreateMovementType(ok=False, message='Type value has to be E or S', movementType=None)

        # validate if already exists
        try:
            exists = MovementType.objects.get(name=params.name)

            if exists is not None:
                return CreateMovementType(ok=False, message='Name already exists', movementType=None)
        except MovementType.DoesNotExist:
            movement_type_instance = MovementType(
                name=params.name,
                type=params.type,
                active=True
            )

            movement_type_instance.save()
            return CreateMovementType(ok=True, movementType=movement_type_instance)


class UpdateMovementType(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)
        params = MovementTypeInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()
    movementType = graphene.Field(MovementTypeTypes)

    def mutate(self, info, identify, params=None):
        movement_type_instance = MovementType.objects.get(pk=identify)

        if movement_type_instance is None:
            return UpdateMovementType(ok=False, message='Movement Type does not exists', movementType=None)

        if params is None:
            return UpdateMovementType(ok=False, message='Params is not defined', movementType=None)

        if params.type is not MovementType.ENTRY and params.type is not MovementType.DEPARTURE:
            return UpdateMovementType(ok=False, message='Type value has to be E or S', movementType=None)

        # validate if already exists
        try:
            exists = MovementType.objects.exclude(pk=identify).get(name=params.name)

            if exists is not None:
                return UpdateMovementType(ok=False, message='Name already exists', movementType=None)
        except MovementType.DoesNotExist:
            movement_type_instance.name = params.name if params.name else movement_type_instance.name
            movement_type_instance.type = params.type if params.type else movement_type_instance.type
            movement_type_instance.active = params.active if params.active else movement_type_instance.active

            movement_type_instance.save()
            return UpdateMovementType(ok=True, movementType=movement_type_instance)


class CreateMovement(graphene.Mutation):
    class Arguments:
        params = MovementInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()
    movement = graphene.Field(MovementTypes)

    def mutate(self, info, params):
        if params is None:
            return CreateMovement(ok=False, message='Params were not provided', movement=None)

        movement_type = MovementType.objects.get(pk=params.movement_type_id)
        inventory = Inventory.objects.get(pk=params.inventory_id)

        if movement_type is None:
            return CreateMovement(ok=False, movement=None)

        if inventory is None:
            return CreateMovement(ok=False, movement=None)

        movement_instance = Movement(
            movement_type=movement_type,
            inventory=inventory,
            date=params.date,
            quantity=params.quantity,
            description=params.description,
            active=True
        )

        movement_instance.save()
        return CreateStore(ok=True, movement=movement_instance)


class UpdateMovement(graphene.Mutation):
    class Arguments:
        identify = graphene.ID(required=True)
        params = MovementInput(required=True)

    ok = graphene.Boolean()
    movement = graphene.Field(MovementTypes)

    def mutate(self, info, identify, params=None):
        movement_instance = Store.objects.get(pk=identify)

        if movement_instance is None:
            return UpdateMovement(ok=False, movement=None)

        if params is None:
            return UpdateMovement(ok=False, movement=None)

        movement_type = MovementType.objects.get(pk=params.movement_type_id)
        inventory = Inventory.objects.get(pk=params.inventory_id)

        if movement_type is None:
            movement_type = movement_instance.movement_type

        if inventory is None:
            inventory = movement_instance.inventory

        movement_instance.movement_type = movement_type
        movement_instance.inventory = inventory
        movement_instance.date = params.date if params.date else movement_instance.date
        movement_instance.description = params.description if params.description else movement_instance.description
        movement_instance.quantity = params.quantity if params.quantity else movement_instance.quantity
        movement_instance.active = params.active if params.active else movement_instance.active

        movement_instance.save()
        return UpdateStore(ok=True, movement=movement_instance)
