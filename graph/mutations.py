import graphene
import graphql_jwt

from category.mutations import CreateCategory, UpdateCategory

from product.mutations import CreateBrand, CreateModel, CreateSize, CreateProduct
from product.mutations import UpdateBrand, UpdateModel, UpdateSize, UpdateProduct

from product_detail.mutations import CreateUnit, CreateColor
from product_detail.mutations import UpdateUnit, UpdateColor

from inventory.mutations import CreateStore, CreateInventory, CreateMovementType, CreateMovement
from inventory.mutations import UpdateStore, UpdateInventory, UpdateMovementType, UpdateMovement

from customer.mutations import CreateCustomer, UpdateCustomer

from sale.mutations import CreateSale, CreateInvoice, UpdateSale, UpdateSaleDetail


# ************** MUTATIONS ************** #
# ************** #

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()

    create_brand = CreateBrand.Field()
    update_brand = UpdateBrand.Field()

    create_model = CreateModel.Field()
    update_model = UpdateModel.Field()

    create_size = CreateSize.Field()
    update_size = UpdateSize.Field()

    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()

    create_color = CreateColor.Field()
    update_color = UpdateColor.Field()

    create_unit = CreateUnit.Field()
    update_unit = UpdateUnit.Field()

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

    create_sale = CreateSale.Field()
    update_sale = UpdateSale.Field()

    create_invoice = CreateInvoice.Field()
    update_sale_detail = UpdateSaleDetail.Field()

