import colander


class FlightQuerystringSchema(colander.MappingSchema):
    origin = colander.SchemaNode(colander.Str())
    destination = colander.SchemaNode(colander.Str())


class AirportSchema(colander.MappingSchema):
    name = colander.SchemaNode(colander.Str(), description='Airport name')
    city = colander.SchemaNode(colander.Str(), description='Aiport city')
    country = colander.SchemaNode(colander.Str(),
                                  description='Airport country')
    iata_3 = colander.SchemaNode(colander.Str(), description='IATA_3')
    latitute = colander.SchemaNode(colander.Str(), description='Latitude')
    longitude = colander.SchemaNode(colander.Str(), description='Longitude')


class AirlineSchema(colander.MappingSchema):
    name = colander.SchemaNode(colander.Str(), description='Airline name')
    two_digit_code = colander.SchemaNode(colander.Str(),
                                         description='2_digit_code')
    three_digit_code = colander.SchemaNode(colander.Str(),
                                           description='3_digit_code')
    country = colander.SchemaNode(colander.Str(),
                                  description='Airline country')


class RouteSchema(colander.MappingSchema):
    origin = AirportSchema(description='Origin of flight')
    destination = AirportSchema(description='Destination of flight')
    airline = AirlineSchema(description='Airline')


class DataSchema(colander.MappingSchema):
    data = colander.SequenceSchema(RouteSchema(), description='Flights')


class Response200(colander.MappingSchema):
    body = DataSchema()


class BadRequestSchema(colander.MappingSchema):
    message = colander.SchemaNode(colander.Str(),
                                  description='Bad request message')
    status = colander.SchemaNode(colander.Str(),
                                 description='Status code message')


class InternalServerErrorSchema(colander.MappingSchema):
    error = colander.SchemaNode(colander.Str(),
                                description='Error message')
    status = colander.SchemaNode(colander.Str(),
                                 description='Status code message')


class Response400(colander.MappingSchema):
    body = BadRequestSchema()


class Response500(colander.MappingSchema):
    body = InternalServerErrorSchema()


response_route_schemas = {
    '200': Response200(description='Success'),
    '400': Response400(description='Bad Request'),
    '5**': Response500(description='Internal server error')
}
