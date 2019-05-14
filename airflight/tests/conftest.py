import os

import mongomock
import pytest
from pyramid import testing
from pyramid.paster import get_appsettings
from pyramid.threadlocal import get_current_registry
from webtest import TestApp
from mock import patch
from airflight import main

here = os.path.dirname(__file__)
settings_file = os.path.join(here, '../../', 'testing.ini')


@pytest.fixture(scope='module', autouse=True)
def settings():
    settings = get_appsettings(settings_file, name='main')
    get_current_registry().settings = dict(settings)
    return settings


@pytest.fixture(scope='session')
def app(request):
    with patch('airflight.collections.base.MongoClient',
               mongomock.MongoClient):
        _settings = get_appsettings(settings_file, name='main')

        config = testing.setUp(settings=_settings)

        config.include('airflight.collections')

        _app = main(_settings.global_conf, **_settings)
        test_app = TestApp(_app)

        yield test_app


@pytest.fixture(scope='session')
def data(app):
    from airflight.collections import AirlineCollection, AirportCollection, \
        RouteCollection
    _airlines_payload = [
        {
            "name": "United Airlines",
            "2_digit_code": "UA",
            "3_digit_code": "UAL",
            "country": "United States"
        },
        {
            "name": "Turkish Airlines",
            "2_digit_code": "TK",
            "3_digit_code": "THY",
            "country": "Turkey"
        },
    ]
    _airports_payload = [
        {
            "name": "Etimesgut Air Base",
            "city": "Ankara",
            "country": "Turkey",
            "iata_3": "ANK",
            "latitute": "39.94979858",
            "longitude": "32.68859863"
        },
        {
            "name": "Adana Airport",
            "city": "Adana",
            "country": "Turkey",
            "iata_3": "ADA",
            "latitute": "36.98220062",
            "longitude": "35.28039932"
        },
        {
            "name": "Victoria Harbour Seaplane Base",
            "city": "Victoria",
            "country": "Canada",
            "iata_3": "YWH",
            "latitute": "48.42498589",
            "longitude": "-123.3888674"
        },
        {
            "name": "Lester B. Pearson International Airport",
            "city": "Toronto",
            "country": "Canada",
            "iata_3": "YYZ",
            "latitute": "43.67720032",
            "longitude": "-79.63059998"
        }
    ]
    _routes_payload = [
        {
            "airline_id": "UA",
            "origin": "YYZ",
            "destination": "YWH"
        },
        {
            "airline_id": "UA",
            "origin": "ANK",
            "destination": "YYZ"
        },
        {
            "airline_id": "UA",
            "origin": "YWH",
            "destination": "ADA"
        },
        {
            "airline_id": "TK",
            "origin": "YYZ",
            "destination": "ADA"
        },
        {
            "airline_id": "TK",
            "origin": "ADA",
            "destination": "ANK"
        },
        {
            "airline_id": "TK",
            "origin": "ANK",
            "destination": "ADA"
        },
        {
            "airline_id": "UA",
            "origin": "YYZ",
            "destination": "ANK"
        },
        {
            "airline_id": "UA",
            "origin": "YWH",
            "destination": "YYZ"
        },
    ]
    RouteCollection().insert_many(_routes_payload)
    AirportCollection().insert_many(_airports_payload)
    AirlineCollection().insert_many(_airlines_payload)
