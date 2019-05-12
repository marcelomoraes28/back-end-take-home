from marshmallow import Schema, fields


class FlightQuerystringSchema(Schema):
    origin = fields.Str(required=True)
    destination = fields.Str(required=True)
