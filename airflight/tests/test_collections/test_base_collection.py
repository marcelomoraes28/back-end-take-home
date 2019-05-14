from bson import ObjectId


class TestBaseCollection:
    def test_insert_base_collection(self, app):
        from airflight.collections.base import BaseCollection

        class AirplaneCollection(BaseCollection):
            collection = 'airplane'

            def insert(self, data):
                return self.db.insert_one(data).inserted_id

            def insert_many(self, data):
                return self.db.insert_many(data).inserted_ids

        airplane_collection = AirplaneCollection()
        _data = {
            "name": "Boing 747",
            "capacity": "95tons"
        }
        _id = airplane_collection.insert(_data)
        assert isinstance(_id, ObjectId)

        _datas = [
            {
                "name": "Boing 777",
                "capacity": "100tons"
            }, {
                "name": "Boing FOO-BAR",
                "capacity": "1000tons"
            }
        ]
        _ids = airplane_collection.insert_many(_datas)
        assert len(_ids) == 2

    def test_get_base_collection(self, app):
        from airflight.collections.base import BaseCollection

        class AirplaneCollection(BaseCollection):
            collection = 'airplane'

            def insert(self, data):
                return self.db.insert_one(data).inserted_id

            def insert_many(self, data):
                return self.db.insert_many(data).inserted_ids

        airplane_collection = AirplaneCollection()
        _data = {
            "name": "Boing 747",
            "capacity": "95tons"
        }
        _id = airplane_collection.insert(_data)
        get_data = airplane_collection.get({"_id": _id})
        assert _data == get_data
