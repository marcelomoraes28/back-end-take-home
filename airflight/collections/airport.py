import pymongo

from airflight.collections.base import BaseCollection


class AirportCollection(BaseCollection):
    collection = 'airports'

    def __init__(self):
        self.db.create_index(
            [("name", pymongo.ASCENDING), ("city", pymongo.ASCENDING),
             ("country", pymongo.ASCENDING), ("iata_3", pymongo.ASCENDING)],
            unique=True)

    def insert(self, data):
        return self.db.insert_one(data).inserted_id
