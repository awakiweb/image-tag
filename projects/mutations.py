import graphene
import base64
from graphql_jwt.decorators import login_required
from django.core.files.base import ContentFile

from .inputs import ProjectInput, ProjectFileInput
from .models import Project, ProjectFile

from cities.models import City


class CreateProject(graphene.Mutation):
    class Arguments:
        params = ProjectInput(required=True)

    id = graphene.Int()
    ok = graphene.Boolean()
    message = graphene.String()

    @login_required
    def mutate(self, info, params):
        if not params:
            return CreateProject(id=0, ok=False, message='Params are invalid')

        city = City.objects.get(pk=params.city_id)
        if city is None:
            return CreateProject(id=0, ok=False, message='This city does not exists')

        new_instance = Project(
            name=params.name,
            city=city,
            active=True
        )

        new_instance.save()
        return CreateProject(id=new_instance.id, ok=True, message='Project created successfully')


class UpdateProject(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)
        params = ProjectInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()

    @login_required
    def mutate(self, info, pk, params):
        if not pk:
            return UpdateProject(ok=False, message='Params are invalid')
        if not params:
            return UpdateProject(ok=False, message='Params are invalid')

        instance = Project.objects.get(pk=pk)
        if instance:
            city = City.objects.get(pk=params.city_id)
            if city is None:
                return CreateProject(id=0, ok=False, message='This city does not exists')

            instance.name = params.name
            instance.city = city
            instance.save()

            return UpdateProject(ok=True, message='Project was updated')
        return UpdateProject(ok=False, message='Project was not found')


class DeleteProject(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)

    ok = graphene.Boolean()
    message = graphene.String()

    @login_required
    def mutate(self, info, pk):
        if not pk:
            return DeleteProject(ok=False, message='Params are invalid')

        instance = Project.objects.get(pk=pk, active=True)
        if instance:
            instance.active = False
            instance.save()

            return DeleteProject(ok=True, message='Project was inactivate')
        return DeleteProject(ok=False, message='Project was not found')


class ActivateProject(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)

    ok = graphene.Boolean()
    message = graphene.String()

    @login_required
    def mutate(self, info, pk):
        if not pk:
            return ActivateProject(ok=False, message='Params are invalid')

        instance = Project.objects.get(pk=pk, active=False)
        if instance:
            instance.active = True
            instance.save()

            return ActivateProject(ok=True, message='Project was activate')
        return ActivateProject(ok=False, message='Project was not found')


class CreateProjectFile(graphene.Mutation):
    class Arguments:
        params = ProjectFileInput(required=True)

    id = graphene.Int()
    ok = graphene.Boolean()
    message = graphene.String()

    @login_required
    def mutate(self, info, params):
        if not params:
            return CreateProjectFile(id=0, ok=False, message='Params are invalid')

        project = Project.objects.get(pk=params.project_id)

        format_geo_json, file_geo_json = params.geo_json_file.split(';base64,')
        format_excel, file_excel = params.excel_file.split(';base64,')

        new_instance = ProjectFile(
            project=project,
            geo_json_file=ContentFile(base64.b64decode(file_geo_json), name=params.geo_json_file_name),
            excel_file=ContentFile(base64.b64decode(file_excel), name=params.excel_file_name),
            active=True
        )

        new_instance.save()
        return CreateProjectFile(id=new_instance.id, ok=True, message='Project Files were added successfully')
