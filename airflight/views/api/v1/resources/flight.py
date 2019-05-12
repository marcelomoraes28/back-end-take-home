from cornice import Service
from cornice.validators import marshmallow_querystring_validator

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
    # TODO: Implement the endpoint
