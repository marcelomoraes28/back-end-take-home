import os
import sys
import csv
import logging

from pymongo.errors import DuplicateKeyError
from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

from pyramid.scripts.common import parse_vars

from airflight.collections import mongo_client_
from ..collections import AirportCollection, AirlineCollection, RouteCollection

logger = logging.getLogger(__name__)


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    """
    Import data into mongo collections
    """
    here = os.path.dirname(__file__)
    # Create file key with absolute path, class and fields
    COLLECTIONS = [
        {'klass': AirlineCollection,
         'file': os.path.join(here, '../../data/airlines.csv'),
         'fields': [
             'name',
             '2_digit_code',
             '3_digit_code',
             'country'
         ]
         },
        {'klass': AirportCollection,
         'file': os.path.join(here, '../../data/airports.csv'),
         'fields': [
             'name',
             'city',
             'country',
             'iata_3',
             'latitute',
             'longitude'
         ]
         },
        {'klass': RouteCollection,
         'file': os.path.join(here, '../../data/routes.csv'),
         'fields': [
             'airline_id',
             'origin',
             'destination'
         ]
         }
    ]

    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    # Setup of MongoClient
    mongo_client_.setup(url=settings.get('mongo.url'),
                        db=settings.get('mongo.db'))
    for collection in COLLECTIONS:

        mongo_collection = collection['klass']()
        with open(collection['file'], 'r') as csv_file:
            fields = collection['fields']
            csv_reader = csv.reader(csv_file, delimiter=',')
            for k, row in enumerate(csv_reader):
                # must ignore the headers
                if k > 0:
                    # Convert to dict using fields
                    to_dict = dict(zip(fields, row))
                    try:
                        mongo_collection.insert(data=to_dict)
                    except DuplicateKeyError as e:
                        logger.info(f"This data already exist {str(to_dict)} \n")  # noqa
