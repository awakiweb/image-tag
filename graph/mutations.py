import graphene

from category.mutations import CreateCategory, UpdateCategory

from product.mutations import CreateBrand, CreateModel, CreateSize, CreateUnit, CreateColor, CreateProduct
from product.mutations import UpdateBrand, UpdateModel, UpdateSize, UpdateUnit, UpdateColor, UpdateProduct

from inventory.mutations import CreateStore, CreateInventory, CreateMovementType, CreateMovement
from inventory.mutations import UpdateStore, UpdateInventory, UpdateMovementType, UpdateMovement

from customer.mutations import CreateCustomer, UpdateCustomer


# ************** MUTATIONS ************** #
# ************** #

class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()

    create_brand = CreateBrand.Field()
    update_brand = UpdateBrand.Field()

    create_model = CreateModel.Field()
    update_model = UpdateModel.Field()

    create_size = CreateSize.Field()
    update_size = UpdateSize.Field()

    create_color = CreateColor.Field()
    update_color = UpdateColor.Field()

    create_unit = CreateUnit.Field()
    update_unit = UpdateUnit.Field()

    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()

    create_store = CreateStore.Field()
    update_store = UpdateStore.Field()

    create_inventory = CreateInventory.Field()
    update_inventory = UpdateInventory.Field()

    create_movement_type = CreateMovementType.Field()
    update_movement_type = UpdateMovementType.Field()

    create_movement = CreateMovement.Field()
    update_movement = UpdateMovement.Field()

    create_customer = CreateCustomer.Field()
    update_customer = UpdateCustomer.Field()

