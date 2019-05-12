from bson import ObjectId


class TestBaseCollection:
    def test_insert_base_collection(self, app):
        from airflight.collections.base import BaseCollection

        class AirplaneCollection(BaseCollection):
            collection = 'airplane'

            def insert(self, data):
                return self.db.insert_one(data).inserted_id

        airplane_collection = AirplaneCollection()
        _data = {
            "name": "Boing 747",
            "capacity": "95tons"
        }
        _id = airplane_collection.insert(_data)
        assert isinstance(_id, ObjectId)

    def test_get_base_collection(self, app):
        from airflight.collections.base import BaseCollection

        class AirplaneCollection(BaseCollection):
            collection = 'airplane'

            def insert(self, data):
                return self.db.insert_one(data).inserted_id

        airplane_collection = AirplaneCollection()
        _data = {
            "name": "Boing 747",
            "capacity": "95tons"
        }
        _id = airplane_collection.insert(_data)
        get_data = airplane_collection.get({"_id": _id})
        assert _data == get_data
