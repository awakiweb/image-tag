import graphene
import base64
from graphql_jwt.decorators import login_required
from django.core.files.base import ContentFile

from .inputs import ProjectInput, ProjectFileInput
from .models import Project, ProjectFile

from cities.models import County, City


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

        # find county
        county = County.objects.get(pk=params.county_id)

        if county is None:
            return CreateProject(id=0, ok=False, message='This county does not exists')

        # find city
        if params.city_id == 0:
            city = None
        else:
            city = City.objects.get(pk=params.city_id)

        if city is None:
            return CreateProject(id=0, ok=False, message='This city does not exists')

        new_instance = Project(
            name=params.name,
            city=city,
            county=county,
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
            if params.city_id == 0:
                city = None
            else:
                city = City.objects.get(pk=params.city_id)

            county = County.objects.get(pk=params.county_id)
            if county is None:
                return CreateProject(id=0, ok=False, message='This city does not exists')

            instance.publish = params.publish
            instance.name = params.name
            instance.county = county
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

        if params.geo_json_file is None or params.excel_file is None:
            return CreateProjectFile(id=0, ok=False, message='Missing files are required')

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


class UpdateProjectFile(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)
        params = ProjectFileInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()

    @login_required
    def mutate(self, info, pk, params):
        if not pk:
            return UpdateProjectFile(ok=False, message='Params are invalid')
        if not params:
            return UpdateProjectFile(ok=False, message='Params are invalid')

        instance = ProjectFile.objects.get(pk=pk)
        if instance:
            # check geo json file exists and replace it
            if params.geo_json_file is not None:
                format_geo_json, file_geo_json = params.geo_json_file.split(';base64,')
                instance.geo_json_file = ContentFile(base64.b64decode(file_geo_json), name=params.geo_json_file_name)

            # check excel file exists and replace it
            if params.excel_file is not None:
                format_excel, file_excel = params.excel_file.split(';base64,')
                instance.excel_file = ContentFile(base64.b64decode(file_excel), name=params.excel_file_name)

            instance.save()

            return UpdateProjectFile(ok=True, message='Project Files was updated')
        return UpdateProjectFile(ok=False, message='Project Files was not found')


class DeleteProjectFile(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)

    ok = graphene.Boolean()
    message = graphene.String()

    @login_required
    def mutate(self, info, pk):
        if not pk:
            return DeleteProjectFile(ok=False, message='Params are invalid')

        instance = ProjectFile.objects.get(pk=pk, active=True)
        if instance:
            instance.active = False
            instance.save()

            return DeleteProjectFile(ok=True, message='File was deleted')
        return DeleteProjectFile(ok=False, message='File was not found')
