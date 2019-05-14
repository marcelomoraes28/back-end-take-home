from cornice import Service
from cornice.validators import colander_querystring_validator
from pyramid.httpexceptions import HTTPBadRequest, HTTPOk, \
    HTTPInternalServerError

from airflight.views.api.v1.flight.exceptions import NoFlightFound, \
    OriginIsTheSameAsTheDestination
from airflight.views.api.v1.flight.flight import FlightAPI
from airflight.views.api.v1.marshmallow_schemas.flight_schemas import \
    FlightQuerystringSchema, response_route_schemas

flight_service = Service(name='flight-service',
                         path='/flight',
                         description="Get Flights")


@flight_service.get(content_type="application/json",
                    validators=colander_querystring_validator,
                    schema=FlightQuerystringSchema,
                    response_schemas=response_route_schemas,
                    tags=['flight'])
def _get_flight(request):
    """
    /api/v1/flight?origin=ABJ&destination=BRU
    """
    try:
        get_best_route = FlightAPI(request).get_best_route()
    except (NoFlightFound, OriginIsTheSameAsTheDestination) as e:
        return HTTPBadRequest(json=e.args[0])
    except Exception as e:
        # For security, do not show the traceback to user
        return HTTPInternalServerError(json={"error": "Internal server error",
                                             "status": HTTPInternalServerError().status_code})  # noqa
    else:
        return HTTPOk(json=get_best_route)
