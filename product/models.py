from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Model(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    brand = models.ForeignKey(Brand, related_name='models', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Size(models.Model):
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Product(models.Model):
    size = models.ForeignKey(Size, related_name='products', on_delete=models.CASCADE)
    model = models.ForeignKey(Model, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey('category.Category', related_name='products', on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    thumb = models.ImageField(upload_to='uploads/products', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products', null=True, blank=True)

    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, related_name='product_prices', on_delete=models.CASCADE)

    PURCHASE_PRICE = 'P'
    SALE_PRICE = 'S'

    PRICE_TYPE_CHOICE = [
        (PURCHASE_PRICE, 'Precio de Compra'),
        (SALE_PRICE, 'Precio de Venta')
    ]

    price_type = models.CharField(choices=PRICE_TYPE_CHOICE, max_length=1)
    price = models.FloatField()

    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "C$ {}".format(self.product.name)
