from peewee import *

# from data.config import DB_NAME, DB_USER, DB_HOST, DB_PASSWORD, DB_PORT

db = SqliteDatabase("Users.db")


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    user_id = BigIntegerField(primary_key=True)
    username = CharField(max_length=200, null=True)

    class Meta:
        db_name = 'users'


class Tariff(BaseModel):
    name = CharField()

    class Meta:
        db_name = 'Tariff'


class Profile(BaseModel):
    # id = BigIntegerField(primary_key=True)
    user = ForeignKeyField(Users, on_delete='CASCADE', backref='profile')
    status = BooleanField(default=False)
    tariff = ForeignKeyField(Tariff, on_delete='CASCADE', null=True)
    start_period = DateTimeField(null=True)
    period = DateTimeField(null=True)

    class Meta:
        db_name = 'Profile'


class TariffPeriod(BaseModel):
    id = ForeignKeyField(Tariff, on_delete='CASCADE')
    tariff = BigIntegerField()
    period = CharField()
    price = FloatField()

    class Meta:
        db_name = 'TariffPeriod'
