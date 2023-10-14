import graphene


class ProjectInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    publish = graphene.Int(required=True)
    city_id = graphene.Int(required=True)
    county_id = graphene.Int(required=True)


class ProjectFileInput(graphene.InputObjectType):
    project_id = graphene.Int(required=True)
    geo_json_file = graphene.String(required=False)
    geo_json_file_name = graphene.String(required=False)
    excel_file = graphene.String(required=False)
    excel_file_name = graphene.String(required=False)
