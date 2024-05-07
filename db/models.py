from uuid import uuid5
from mongoengine import Document,StringField , BooleanField,DateTimeField,UUIDField,ImageField,URLField,DateField,ReferenceField,ListField

class Provider(Document):
    slug = StringField(max_length=100,required=True,unique=True)
    name = StringField(max_length=100,required=True,unique=True)
    is_active = BooleanField(default=True)
    run_date = DateTimeField(required=True)
    last_slug = StringField(unique=True)


class JobPosition(Document):
    title = StringField(max_length=300, required=True)
    slug = StringField(max_length=100,required=True,unique=True)
    company_city = StringField(max_length=200,required=True)
    company_name = StringField(max_length=200,required=True)
    cover = URLField(required=True)
    url_detail = URLField(required=True)
    date = DateField()
    is_active = BooleanField(default=True)
    type_cooperation = StringField(max_length=100,required=False)
    provider = ReferenceField(Provider)


    def job_position_count(self):
        ...