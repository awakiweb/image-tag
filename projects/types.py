import graphene
from graphene_django.types import DjangoObjectType
from .models import Project, ProjectFile


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project


class ProjectFileType(DjangoObjectType):
    geo_json_file_url = graphene.String()
    excel_file_url = graphene.String()

    class Meta:
        model = ProjectFile

    def resolve_geo_json_file_url(self, info):
        return info.context.build_absolute_uri(self.geo_json_file_url())

    def resolve_excel_file_url(self, info):
        return info.context.build_absolute_uri(self.excel_file_url())
