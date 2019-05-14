from cornice import Service
from cornice.validators import marshmallow_querystring_validator
from pyramid.httpexceptions import HTTPBadRequest, HTTPOk, \
    HTTPInternalServerError

from airflight.views.api.v1.flight.exceptions import NoFlightFound, \
    OriginIsTheSameAsTheDestination
from airflight.views.api.v1.flight.flight import FlightAPI
from airflight.views.api.v1.marshmallow_schemas.flight_schemas import \
    FlightQuerystringSchema

flight_service = Service(name='flight_service', path='/flight',
                         description="Get Flights")


@flight_service.get(content_type="application/json",
                    validators=marshmallow_querystring_validator,
                    schema=FlightQuerystringSchema)
def _get_flight(request):
    """
    /api/v1/flight?origin=ABJ&destination=BRU
    """
    try:
        get_best_route = FlightAPI(request).get_best_route()
    except (NoFlightFound, OriginIsTheSameAsTheDestination) as e:
        return HTTPBadRequest(json=e.args[0])
    except Exception as e:
        return HTTPInternalServerError(json={"error": "Internal server error",
                                             "status": HTTPInternalServerError().status_code})  # noqa
    else:
        HTTPOk(json=get_best_route)
