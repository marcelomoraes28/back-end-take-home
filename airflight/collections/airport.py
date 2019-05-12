from airflight.collections.base import BaseCollection


class AirportCollection(BaseCollection):
    collection = 'airports'

    def insert(self, data):
        # TODO: Create index
        return self.db.insert_one(data).inserted_id
