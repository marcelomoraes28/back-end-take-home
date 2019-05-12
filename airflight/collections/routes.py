from airflight.collections.base import BaseCollection


class RouteCollection(BaseCollection):
    collection = 'routes'

    def insert(self, data):
        # TODO: Create index
        return self.db.insert_one(data).inserted_id
