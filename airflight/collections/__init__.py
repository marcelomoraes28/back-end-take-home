from airflight.collections.base import mongo_client_


def includeme(config):
    """
    Initialize the MongoDB Client.
    """
    settings = config.get_settings()
    mongo_client_.setup(url=settings.get('mongo.url'),
                        db=settings.get('mongo.db'))
