from pprint import pprint

from aiogram import Dispatcher
from aiogram.types import *

from database.connections import *
from keyboards.default.menu import menu_btn
from keyboards.inline.choose_keyboard import *
from loader import dp
from utils.misc.plan_tuple import *


async def bot_start(msg: Message):
    user_id = msg.from_user.id
    username = msg.from_user.username
    await add_user(user_id, username)
    # await profile_add_user(user_id)
    btn = await menu_btn()
    await msg.answer(f"Привет, {msg.from_user.full_name}!", reply_markup=btn)


async def user_profil_handler(msg: Message):
    user_id = msg.from_user.id
    # profil = await get_profile_handler(user_id)
    # pprint(profil)
    await msg.answer(f"Profil: id \n\n"
                     f"Tarifingiz: \n\n"
                     f"Tanlangan tarif turi: oylik/Yilik \n\n"
                     f"Paket tugash muddati: \n\n"
                     f"Tarif sotib olingan sana: \n\n"
                     f"Status : \n\n")

#
# async def add_plan_handler(msg: Message):
#     tariflar = await get_tariff_period()
#     tariflar_name = await rate_tariff(tariflar)
#     btn = await choose_plan_menu_btn(tariflar_name)
#     await msg.answer(f"Tarifni tanlang", reply_markup=btn)
#
#
# async def choose_plan_callback_handler(call: CallbackQuery):
#     tariflar = await get_tariff_period()
#     tariflar_muddat = await rate_muddat(tariflar)
#     btn = await inline_choose_plan(tariflar_muddat)
#     await call.message.edit_text("Tarif muddatini tanlang", reply_markup=btn)
#
#
# async def click_choose_type_callback_handler(call: CallbackQuery):
#     await call.answer()
#     btn = await inline_choose_payment()
#     await call.message.edit_text(f"Tolov turini tanlang", reply_markup=btn)


def register_users_py(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])
    dp.register_message_handler(user_profil_handler, regexp='Profil')
    # dp.register_message_handler(add_plan_handler, regexp='A`zo bolish')
    #
    # dp.register_callback_query_handler(click_choose_type_callback_handler, text_contains='tolov:')
    # dp.register_callback_query_handler(choose_plan_callback_handler, text_contains='plan:')
