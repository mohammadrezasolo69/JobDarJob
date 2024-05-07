from mongoengine import connect, disconnect
from config import settings


class _DatabaseConnection:
    def __init__(self):
        self.connection = None
        self.connect_to_db()

    def connect_to_db(self):
        if self.connection is None:
            try:
                db = connect(
                    settings.mongo.database,
                    host=settings.mongo.host,
                    port=settings.mongo.port,
                    username=settings.mongo.username,
                    password=settings.mongo.password
                )
                self.connection = db
                print(f"Connected to MongoDB database: {settings.mongo.database}")
            except Exception as e:
                print(f"Failed to connect to MongoDB database: {e}")


def connect_to_db():
    return _DatabaseConnection()
