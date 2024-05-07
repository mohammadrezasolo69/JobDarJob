from mongoengine import connect, disconnect
from config import settings


def connect_to_db():
    try:
        connect(db=settings.mongo.database)
        print(f"Connected to MongoDB database: {settings.mongo.database}")
    except Exception as e:
        print(f"Failed to connect to MongoDB database: {e}")


def close_connection_db():
    try:
        disconnect()
        print("Disconnected from MongoDB database")
    except Exception as e:
        print(f"Failed to disconnect from MongoDB database: {e}")
