class TestGetFlight:
    def test_get_flight(self, app, data):
        app.get("/api/v1/flight?origin=YWH&destination=ADA", status=200)

    def test_get_flight_route_does_not_exist(self, app):
        app.get("/api/v1/flight?origin=GRU&destination=YYZ", status=400)

    def test_get_flight_origin_is_the_same_as_destination(self, app):
        app.get("/api/v1/flight?origin=YYZ&destination=YYZ", status=400)
