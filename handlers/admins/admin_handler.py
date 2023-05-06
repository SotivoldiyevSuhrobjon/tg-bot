from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import *

from data.config import ADMINS
from database.connections import *
from keyboards.default.admin_menu_btn import admin_add_rate_btn
from keyboards.default.menu import *
from loader import dp
from states.AllStates import Rate_state


async def admin_start(msg: Message):
    user_id = msg.from_user.id
    if user_id in ADMINS:
        btn = await admin_add_rate_btn()
        await msg.answer(f"salom siz admin paneldasiz", reply_markup=btn)

#
# async def add_rate_handler(msg: Message, state: FSMContext):
#     await msg.answer("iltimos tarif nomini kiriting")
#     await Rate_state.name.set()
#
#
# async def choose_month_handler(msg: Message, state: FSMContext):
#     text = msg.text
#     await state.update_data(name=text)
#     btn = await rate_options_btn()
#     await msg.answer("Iltimos tugmani tanlang", reply_markup=btn)
#     await Rate_state.oy.set()
#
#
# async def choose_muddat_callback_handler(call: CallbackQuery, state: FSMContext):
#     await call.answer()
#     oy = call.data.split(":")[-1]
#     await state.update_data(oy=oy)
#     await call.message.answer(f"Siz {oy} ni tanladingiz Iltimos muddatini kiriting raqamlarda")
#     await Rate_state.muddat.set()
#
#
# async def choose_price_handler(msg: Message, state: FSMContext):
#     muddat = msg.text
#     await state.update_data(muddat=muddat)
#     await msg.answer("Iltimos narxni kiriting so'mda ")
#     await Rate_state.narx.set()
#
#
# async def all_save_rate(msg: Message, state: FSMContext):
#     narx = msg.text
#     await state.update_data(narx=narx)
#     data = await state.get_data()
#     btn = await rate_verify_btn()
#     await msg.answer(f"Tarif nomi: <b>{data['name']}</b>\n\n"
#                      f"Tarif muddati: <b>{data['muddat']} {data['oy']}</b>\n\n"
#                      f"Tarif narxi: <b>{data['narx']} so`m</b>\n\n", reply_markup=btn)
#     await Rate_state.save.set()
#
#
# async def verify_state_save_callback_handler(call: CallbackQuery, state: FSMContext):
#     text = call.data.split(":")
#
#     if text == 'delete':
#         await call.answer("Bekor qilindi")
#         await state.finish()
#     else:
#         data = await state.get_data()
#         await call.answer("Saqlandi")
#         await get_add_tariff_period(
#             user_id=call.message.from_user.id,
#             tariff=f"{data['name']}",
#             period=f"{data['muddat']}/{data['oy']}",
#             price=f"{data['narx']}"
#         )
#         await state.reset_state()
#

def admin_register_py(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=['admin'])
    # dp.register_message_handler(add_rate_handler, text=['Tarif qoshish'])
    #
    # dp.register_message_handler(choose_month_handler, state=Rate_state.name)
    # dp.register_message_handler(choose_price_handler, state=Rate_state.muddat)
    # dp.register_message_handler(all_save_rate, state=Rate_state.narx)
    #
    # dp.register_callback_query_handler(choose_muddat_callback_handler, state=Rate_state.oy, text_contains='rate')
    # dp.register_callback_query_handler(verify_state_save_callback_handler, state=Rate_state.save,
    #                                    text_contains='rate:')
