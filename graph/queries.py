import graphene
from graphene_django.types import ObjectType

from graphql_jwt.decorators import login_required

from counties.models import County
from counties.types import CountyType

from cities.models import City
from cities.types import CityType

from projects.models import Project, ProjectFile
from projects.types import ProjectType, ProjectFileType

from excel_columns.models import ExcelColumn
from excel_columns.types import ExcelColumnType

from resources.models import Resource
from resources.types import ResourceType

from customers.models import Customer
from customers.types import CustomerType


# ************** QUERY MODELS ************** #
# ************** #
class Query(ObjectType):
    counties = graphene.List(CountyType)
    cities = graphene.List(CityType)

    projects = graphene.List(ProjectType)
    project_files = graphene.List(ProjectFileType)

    excel_columns = graphene.List(ExcelColumnType)
    resources = graphene.List(ResourceType)

    customers = graphene.List(CustomerType)

    @login_required
    def resolve_counties(self, info, **kwargs):
        return County.objects.all()

    @login_required
    def resolve_cities(self, info, **kwargs):
        return City.objects.all()

    @login_required
    def resolve_projects(self, info, **kwargs):
        return Project.objects.filter(active=True)

    def resolve_project_files(self, info, **kwargs):
        return ProjectFile.objects.filter(active=True, project__active=True, project__publish=True)

    def resolve_excel_columns(self, info, **kwargs):
        return ExcelColumn.objects.all()

    def resolve_resources(self, info, **kwargs):
        return Resource.objects.all()

    @login_required
    def resolve_customers(self, info, **kwargs):
        return Customer.objects.filter(active=True)
