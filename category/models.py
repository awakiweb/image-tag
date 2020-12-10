from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    level = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    parent = models.ForeignKey('self', related_name='categories', null=True, blank=True, on_delete=models.CASCADE)

    thumb = models.ImageField(upload_to='uploads/categories', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/categories', null=True, blank=True)

    order = models.IntegerField(default=0)
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
