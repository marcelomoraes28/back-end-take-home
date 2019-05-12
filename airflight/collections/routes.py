import pymongo

from airflight.collections.base import BaseCollection


class RouteCollection(BaseCollection):
    collection = 'routes'

    def __init__(self):
        self.db.create_index(
            [("airline_id", pymongo.ASCENDING), ("origin", pymongo.ASCENDING),
             ("destination", pymongo.ASCENDING)],
            unique=True)

    def insert(self, data):
        return self.db.insert_one(data).inserted_id
