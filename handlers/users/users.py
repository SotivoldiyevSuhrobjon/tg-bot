from aiogram import Dispatcher
from aiogram.types import *

from database.connections import add_user
from keyboards.default.menu import menu_btn
from keyboards.inline.choose_keyboard import inline_choose_payment, inline_choose_plan
from loader import dp


async def bot_start(msg: Message):
    user_id = msg.from_user.id
    username = msg.from_user.username
    await add_user(user_id, username)
    btn = await menu_btn()
    await msg.answer(f"Привет, {msg.from_user.full_name}!", reply_markup=btn)
    btn = await inline_choose_plan()
    await msg.answer(f"Tarifni tanlang", reply_markup=btn)


async def user_profil_handler(msg: Message):
    await msg.answer(f"Profil: id \n\n"
                     f"Tarifingiz: \n\n"
                     f"Paket tugash muddati: \n\n")


async def add_plan_handler(msg: Message):
    btn = await inline_choose_plan()
    await msg.answer(f"Tarifni tanlang", reply_markup=btn)


async def click_choose_type_callback(call: CallbackQuery):
    await call.answer()
    btn = await inline_choose_payment()
    await call.message.edit_text(f"Tolov turini tanlang", reply_markup=btn)


def register_users_py(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])
    dp.register_message_handler(user_profil_handler, regexp='Profil')
    dp.register_message_handler(add_plan_handler, regexp='A`zo bolish')

    dp.register_callback_query_handler(click_choose_type_callback, text_contains='tolov:')

