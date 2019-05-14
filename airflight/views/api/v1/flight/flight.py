from pyramid.httpexceptions import HTTPBadRequest

from airflight.collections import RouteCollection, AirportCollection, \
    AirlineCollection
from airflight.views.api.v1.flight.exceptions import NoFlightFound, \
    OriginIsTheSameAsTheDestination


class FlightAPI(object):
    """
    Flight API
    """
    MAX_DEPTH = 10  # max number of connections by flight

    def __init__(self, request):
        self.request = request
        self.data = {}
        self.origin = request.matchdict['origin']
        self.destination = request.matchdict['destination']
        if self.origin == self.destination:
            raise OriginIsTheSameAsTheDestination(
                {"message": "The origin can not be the same as destination",
                 "status": HTTPBadRequest})

    def get_best_route(self):
        self._get_routes()
        self._update_data()
        return self.data

    def _update_data(self):
        """
        Update the best route with the information of airlines and airports.
        """
        new_data = []
        for k, data in self.data.items():
            if data[-1]['origin'] == self.origin:
                new_data.append(data)
        if not new_data:
            raise NoFlightFound(
                {"message": "Route not found", "status": HTTPBadRequest})
        # Ordering data by number of elements
        new_data.sort(key=lambda x: len(x))
        # Set the list reversed
        best_route = new_data[0][::-1]
        for route in best_route:
            airline_id = route.pop('airline_id')
            route['airline'] = self.get_airline(airline_id)
            route['origin'] = self.get_airport(route['origin'])
            route['destination'] = self.get_airport(route['destination'])
        self.data = {"data": best_route}

    def _get_routes(self):
        """
        Get all possible routes
        Important:
            MAX_DEPTH by default is 10
            Be careful with MAX_DEPTH not to exceed the maximum
            number of iterations
        """
        # Get all routes with set destination
        destinations = RouteCollection().get_many(
            {'destination': self.destination}, {"_id": 0})
        for k, destination in enumerate(destinations):
            # Append the routes
            self.data[k] = []
            self.data[k].append(destination)
            # If origin is the same as that defined then stop the interaction
            if destination['origin'] == self.origin:
                return
        max_depth = self.MAX_DEPTH
        while max_depth != 0:
            for k, v in self.data.items():
                # Get all destination using the last index of items
                destinations = RouteCollection().get_many(
                    {'destination': v[-1]['origin']}, {"_id": 0})
                for destination in destinations:
                    # If origin is the same as that defined then stop the interaction
                    if destination['origin'] == self.origin:
                        self.data[k].append(destination)
                        return
                    # If the current destination is the last origin then append
                    elif destination['destination'] == v[-1]['origin']:
                        self.data[k].append(destination)
            max_depth -= 1

    def get_airline(self, code):
        """
        Get airline
        :param code: 2_digit_code
        :return: The airline collection
        """
        return AirlineCollection().get({'2_digit_code': code}, {"_id": 0})

    def get_airport(self, iata_3):
        """
        Get the airport
        :param iata_3:
        :return: The airport collection
        """
        return AirportCollection().get({'iata_3': iata_3}, {"_id": 0})
