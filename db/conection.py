from mongoengine import connect
from config import settings

# Database Config
connect(
    settings.mongo.database,
    host=settings.mongo.host,
    port=settings.mongo.port,
    username=settings.mongo.username,
    password=settings.mongo.password,
)
