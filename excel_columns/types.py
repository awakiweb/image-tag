from graphene_django.types import DjangoObjectType
from .models import ExcelColumn


class ExcelColumnType(DjangoObjectType):
    class Meta:
        model = ExcelColumn
