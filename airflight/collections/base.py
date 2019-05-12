from abc import ABCMeta, abstractmethod

from bson import ObjectId
from pymongo import MongoClient


class MongoCli(object):
    """
    MongoClient
    """

    def setup(self, url, db):
        try:
            client = MongoClient(url)
        except Exception as e:
            pass
        else:
            self._con = client[db]

    @property
    def con(self):
        return self._con


mongo_client_ = MongoCli()


class BaseCollection(object, metaclass=ABCMeta):
    """
    Interface to connect in mongodb
    Usage example:
        class CarsCollection(BaseCollection):
            collection = 'cars'
            def insert(data):
                return self.db.insert_one(data).inserted_id
    """
    collection = None
    mongo_cli = mongo_client_

    @property
    def db(self):
        return self.mongo_cli.con[self.collection]

    def get(self, condition):
        """
        Get register from a collection
        :param condition: {"name": "foo-bar"}
        :return: {"_id": ObjectId('5cd81989fba44b8858774d0b'),
                  "name": "foo-bar", ...}
        """
        if "_id" in condition and isinstance(condition["_id"], str):
            condition["_id"] = ObjectId(condition["_id"])
        return self.db.find_one(condition)

    @abstractmethod
    def insert(self, data):
        pass
