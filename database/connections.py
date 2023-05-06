from playhouse.shortcuts import model_to_dict

from data.config import ADMINS
from .models import *


async def add_user(user_id: int, username: str):
    with db:
        if not Users.select().where(Users.user_id == user_id).exists():
            Users.create(user_id=user_id, username=username)


async def get_add_tarif_name(user_id, name):
    with db:
        Tariff.create(id=user_id, name=name)


async def get_add_tariff_period(tariff, period, price):
    with db:
        TariffPeriod.create(id=user_id, tariff=tariff, period=period, price=price)

# async def get_profile_handler(user_id):
#     with db:
#         user = Users.get(Users.id == user_id)
#         profile = Profile.select().join(Users).where(Users.id == user_id)


# async def get_add_tariff_period(user_id, tariff, period, price):
#     with db:
#         TariffPeriod.create(user_id=user_id, tariff=tariff, period=period, price=price)
#
#
# async def get_tariff_period():
#     with db:
#         tar = TariffPeriod.select().where(TariffPeriod.id)
#         tarif = [model_to_dict(item) for item in tar]
#         return tarif
#
#
# async def profile_add_user(user: int):
#     with db:
#         if not Users.select().where(Users.user_id == user).exists():
#             Profile.create(user_id=user, status=None, tariff=None, start_period=None, period=None)
#
#
# async def get_profile_data():
#     with db:
#         users = [model_to_dict(item) for item in
#                  Profile.select(Profile.id, Profile.user, Profile.status, Profile.tariff, Profile.start_period,
#                                 Profile.period)]
#         return users
