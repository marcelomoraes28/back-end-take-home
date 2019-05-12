from airflight.collections.base import BaseCollection


class AirlineCollection(BaseCollection):
    collection = 'airlines'

    def insert(self, data):
        # TODO: Create index
        return self.db.insert_one(data).inserted_id
