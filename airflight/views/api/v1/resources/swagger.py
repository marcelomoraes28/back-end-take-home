from cornice import Service
from cornice.service import get_services
from cornice_swagger import CorniceSwagger

swagger = Service(name='swagger',
                  path='/__api__',
                  description="OpenAPI documentation")

swagger_ui = Service(name='swagger-ui',
                     path='/apidocs',
                     description="OpenAPI documentation")

AVAILABLE_SERVICES = ['flight-service']


def get_services_():
    return [service for service in get_services() if
            service.name in AVAILABLE_SERVICES]


@swagger.get()
def openAPI_spec(request):
    doc = CorniceSwagger(get_services_())
    my_spec = doc.generate('Flight API', '1.0.0', base_path='/api/v1')
    return my_spec


@swagger_ui.get(renderer='../../templates/swagger.jinja2')
def apidocs(request):
    return {}
