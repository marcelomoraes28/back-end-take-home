import pymongo

from airflight.collections.base import BaseCollection


class AirlineCollection(BaseCollection):
    collection = 'airlines'

    def __init__(self):
        self.db.create_index(
            [("name", pymongo.ASCENDING), ("2_digit_code", pymongo.ASCENDING),
             ("3_digit_code", pymongo.ASCENDING),
             ("country", pymongo.ASCENDING)],
            unique=True)

    def insert(self, data):
        return self.db.insert_one(data).inserted_id
