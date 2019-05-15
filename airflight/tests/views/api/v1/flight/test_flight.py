import pytest
from pyramid.testing import DummyRequest
from webob.multidict import MultiDict

from airflight.views.api.v1.flight.exceptions import \
    OriginIsTheSameAsTheDestination


class TestAPIFlight:
    def test_get_route_without_connections(self, app, data):
        """
        Get best route without connections when the airline is United Airlines
        """
        from airflight.views.api.v1.flight.flight import FlightAPI
        req = DummyRequest(method='GET')
        req.params = MultiDict([('origin', 'ANK'), ('destination', 'YYZ')])
        get_route = FlightAPI(req).get_best_route()
        assert len(get_route['data']) == 1
        assert get_route['data'][0]['airline'] == {'name': 'United Airlines',
                                                   '2_digit_code': 'UA',
                                                   '3_digit_code': 'UAL',
                                                   'country': 'United States'}

    def test_get_route_with_two_connections(self, app, data):
        """
            Get best route with two connections when the airlines origin is
            United Airlinesand the connection is Turkish Airlines
        """
        from airflight.views.api.v1.flight.flight import FlightAPI
        req = DummyRequest(method='GET')
        req.params = MultiDict([('origin', 'YWH'), ('destination', 'ANK')])
        get_route = FlightAPI(req).get_best_route()
        assert len(get_route['data']) == 2
        assert get_route['data'][0]['airline'] == {'name': 'United Airlines',
                                                   '2_digit_code': 'UA',
                                                   '3_digit_code': 'UAL',
                                                   'country': 'United States'}

        assert get_route['data'][1]['airline'] == {'name': 'Turkish Airlines',
                                                   '2_digit_code': 'TK',
                                                   '3_digit_code': 'THY',
                                                   'country': 'Turkey'}

    def test_get_route_when_exist_two_different_routes(self, app, data):
        """
        Test when exist different routes
        Route 1: (YWH -> YYZ) -> (YYZ -> ANK) -> (ANK -> ADA)
        Route 2: (YWH -> ADA)

        In this case the system chooses Route 2
        """
        from airflight.views.api.v1.flight.flight import FlightAPI
        req = DummyRequest(method='GET')
        req.params = MultiDict([('origin', 'YWH'), ('destination', 'ADA')])
        get_route = FlightAPI(req).get_best_route()
        assert len(get_route['data']) == 1

    def test_get_route_origin_is_the_same_as_destination(self, app):
        from airflight.views.api.v1.flight.flight import FlightAPI
        req = DummyRequest(method='GET')
        req.params = MultiDict([('origin', 'YWH'), ('destination', 'YWH')])
        with pytest.raises(OriginIsTheSameAsTheDestination):
            FlightAPI(req).get_best_route()
