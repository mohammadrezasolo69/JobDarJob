from mongoengine import Document,StringField , BooleanField,DateTimeField,UUIDField,ImageField,URLField,DateField,ReferenceField,ListField

class Provider(Document):
    id = UUIDField()
    name = StringField(max_length=100,required=True,unique=True)
    is_active = BooleanField(default=True)
    run_date = DateTimeField(required=True)
    last_slug = StringField(unique=True)


class JobPosition(Document):
    id = UUIDField()
    title = StringField(max_length=300,required=True)
    company_city = StringField(max_length=200,required=True)
    company_name = StringField(max_length=200,required=True)
    cover = ImageField(required=True)
    url = URLField(required=True)
    date = DateField(required=True)
    provider = ReferenceField(Provider)
    is_active = BooleanField(default=True)
    expired_date = DateField(required=True)
    category = ListField(required=False)
    type_cooperation = StringField(max_length=100,required=False)


    def job_position_count(self):
        ...