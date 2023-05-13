from pprint import pprint

from playhouse.shortcuts import model_to_dict

from data.config import ADMINS
from .models import *


async def add_user(user_id: int, username: str):
    with db:
        if not Users.select().where(Users.user_id == user_id).exists():
            Users.create(user_id=user_id, username=username)


async def get_add_tarif_name(name):
    with db:
        Tariff.create(name=name)


async def get_add_tariff_period(data):
    with db:
        m = Tariff.select().where(Tariff.name == f"{data['name']}")
        name = [model_to_dict(item) for item in m]
        key_list = list(data.keys())
        if 'oy' in data.keys():
            for item in data['oy']:
                TariffPeriod.create(
                    tariff=name[0]['id'],
                    period=f"{item[0]}/{key_list[2]}",
                    price=f"{item[1]}"
                )
        if 'yil' in data.keys():
            for item in data['yil']:
                TariffPeriod.create(
                    tariff=name[0]['id'],
                    period=f"{item[0]}/{key_list[2]}",
                    price=f"{item[1]}"
                )


async def get_rate_name():
    with db:
        tar = Tariff.select().where(Tariff.id)
        tarif = [model_to_dict(item) for item in tar]
        return tarif


async def tariff_period_get_btn(text):
    with db:
        per = TariffPeriod.select().where(TariffPeriod.tariff_id)
        period = [model_to_dict(item) for item in per]
        data = []
        for item in period:
            if item["tariff"]["name"] == text[0]:
                btn_id = data.append([item["period"], item["price"]])
        return data


# async def profile_data(user_id):
#     with db:
#         user = Users.get(Users.user_id == user_id)
#         profile = Profile.select().join(Users).where(Users.user_id == user_id)
#         prof = [model_to_dict(item) for item in profile]
#

async def get_tariff_period():
    with db:
        tar = TariffPeriod.select().where(TariffPeriod.id)
        tarif = [model_to_dict(item) for item in tar]
        return tarif


async def get_profile_create(user_id, tariff_id, start_period, period):
    with db:
        Profile.create(
            user_id=user_id,
            status=False,
            tariff_id=tariff_id,
            start_period=start_period,
            period=period)


async def get_tariff_period_delete():
    with db:
        tar = TariffPeriod.select().where(TariffPeriod.tariff_id)
        tarifperiod = [model_to_dict(item) for item in tar]
        return tarifperiod


async def delete_tariff_period(user_id):
    with db:
        TariffPeriod.delete().where(TariffPeriod.delete_by_id(user_id))
        if not TariffPeriod.select().where(TariffPeriod.tariff == user_id).exists():
            Tariff.delete().where(Tariff.id == user_id).execute()
