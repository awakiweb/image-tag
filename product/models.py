from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    order = models.IntegerField()
    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

        ordering = ['order']

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse('category_list')


class Subcategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    order = models.IntegerField()
    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'

        ordering = ['order']

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse('subcategory_list')


class Brand(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Size(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)

class Unit(models.Model):
    name = models.CharField(max_length=150)
    symbol = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)

    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Color(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Product(models.Model):
    size = models.ForeignKey(Size, related_name='products', on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, related_name='products', on_delete=models.CASCADE)
    color = models.ForeignKey(Color, related_name='products', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='products', on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    thumb = models.ImageField(upload_to='uploads/products', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/category', null=True, blank=True)

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
