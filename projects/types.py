import graphene
from graphene_django.types import DjangoObjectType
from .models import Project, ProjectFile


class ProjectFileType(DjangoObjectType):
    geo_json_file_url = graphene.String()
    excel_file_url = graphene.String()

    class Meta:
        model = ProjectFile

    def resolve_geo_json_file_url(self, info):
        return info.context.build_absolute_uri(self.geo_json_file_url())

    def resolve_excel_file_url(self, info):
        return info.context.build_absolute_uri(self.excel_file_url())


class ProjectType(DjangoObjectType):
    active_files = graphene.List(ProjectFileType)

    class Meta:
        model = Project

    def resolve_active_files(self, info):
        return self.active_files()
