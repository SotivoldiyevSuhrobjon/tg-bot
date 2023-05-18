import types
from datetime import datetime
from pprint import pprint

from aiogram import Dispatcher
from aiogram.types import *
from aiogram.types.message import ContentTypes, Message
from aiogram.dispatcher import FSMContext

from database.connections import *
from keyboards.default.users_menu import menu_btn
from keyboards.inline.choose_keyboard import *
from loader import dp
from utils.misc.plan_tuple import *
from states.AllStates import *


# prices = [
#     types.LabeledPrice(label='Working Time Machine', amount=5750),
#     types.LabeledPrice(label='Gift wrapping', amount=500),
# ]
#
# shipping_options = [
#     types.ShippingOption(id='instant', title='WorldWide Teleporter').add(types.LabeledPrice('Teleporter', 1000)),
#     types.ShippingOption(id='pickup', title='Local pickup').add(types.LabeledPrice('Pickup', 300)),
# ]


async def bot_start(msg: Message):
    user_id = msg.from_user.id
    username = msg.from_user.username
    await add_user(user_id, username)
    # await profile_add_user(user_id)
    btn = await menu_btn()
    await msg.answer(f"Привет, {msg.from_user.full_name}!", reply_markup=btn)


async def user_profile_handler(msg: Message):
    user_id = msg.from_user.id
    prof = Profile.select().where(Profile.user_id == user_id)
    profile = [model_to_dict(item) for item in prof]
    # if profile:
    #     userni
    #     malumotlari
    # else:
    #     sizda
    #     malumot
    #     yoq
    if profile:
        for item in profile:
            if item['status'] == True:
                await msg.answer(f"👤 Profil id:  \n\n"
                                 f"♻️ Tarifingiz: \n\n"
                                 f"🖌 Tanlangan tarif turi: \n\n"
                                 f"⚠️ Paket tugash muddati: \n\n"
                                 f"🕐 Tarif sotib olingan sana: \n\n"
                                 f"✅ Status : \n\n")
                break
            else:
                await msg.answer(f"👤 Profil: {user_id} \n\n"
                                 f"♻️ Tarifingiz: <b>Ulanmagan</b>\n\n"
                                 f"🖌 Tanlangan tarif turi: <b>Ulanmagan</b> \n\n"
                                 f"⚠️ Paket tugash muddati: <b>Ulanmagan</b>\n\n"
                                 f"🕐 Tarif sotib olingan sana: <b>Ulanmagan</b> \n\n"
                                 f"❌ Status : <b>Ulanmagan</b>\n\n")
                break
    else:
        await msg.answer(f"👤 Profil: {user_id} \n\n"
                         f"♻️ Tarifingiz: <b>Ulanmagan</b>\n\n"
                         f"🖌 Tanlangan tarif turi: <b>Ulanmagan</b> \n\n"
                         f"⚠️ Paket tugash muddati: <b>Ulanmagan</b>\n\n"
                         f"🕐 Tarif sotib olingan sana: <b>Ulanmagan</b> \n\n"
                         f"❌ Status : <b>Ulanmagan</b>\n\n")


async def add_plan_rate_handler(msg: Message, state: FSMContext):
    tariflar = await get_rate_name()
    if tariflar:
        # tariflar is select Tariff name
        tariflar_name = await rate_tariff(tariflar)
        # tariflar name name and id list tuple
        # btn is tariflar name is id and name
        btn = await choose_plan_menu_btn(tariflar_name)
        await msg.answer(f"♻️Tarifni tanlang♻️", reply_markup=btn)
        await Save_plan.tarif_name.set()
    else:
        await msg.answer("Tariflar qoshilmagan")
        await state.finish()


async def choose_plan_callback_handler(call: CallbackQuery, state: FSMContext):
    cal = call.data.split(":")
    id = cal[1]
    text = id.split("/")
    await state.update_data(tarif_name=text)
    plan = await tariff_period_get_btn(text)
    btn = await inline_choose_plan(plan)
    await call.message.edit_text("🕐 Tarif muddatini tanlang", reply_markup=btn)
    await Save_plan.tarif_rate.set()


async def click_choose_type_callback_handler(call: CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    cal = call.data.split(":")
    data = cal[1].split("/")
    await state.update_data(tarif_rate=data)
    about = await state.get_data()
    import datetime

    # Get the current time
    now = datetime.datetime.now()
    # Get the tariff rate from the dictionary
    duration, unit = about['tarif_rate'][0], about['tarif_rate'][1]

    # Calculate the end date based on the duration and unit
    if unit == 'oy':
        end_date = now + datetime.timedelta(days=30 * int(duration))
    elif unit == 'yil':
        end_date = now + datetime.timedelta(days=365 * int(duration))
    else:
        raise ValueError('Invalid unit: {}'.format(unit))
    a = await state.get_data()
    # await get_profile_create(
    #     user_id=user_id,
    #     tariff_id=f"{about['tarif_name'][1]}",
    #     start_period=now,
    #     period=end_date
    # )
    await call.answer()
    btn = await inline_choose_payment()
    await call.message.edit_text(f"📝 Tarif nomi: {about['tarif_name'][0]}\n\n"
                                 f"🕐 Tarif muddati: {about['tarif_rate'][0]}/{about['tarif_rate'][1]}\n\n"
                                 f"💵 Tarif narxi:  {about['tarif_rate'][-1]}\n\n"
                                 f"🎉 Tarif boshlanish vaqti: {now}\n\n"
                                 f"⚠️ Tarif tugash vaqti: {end_date}\n\n"
                                 f"💳 Tolov turini tanlang", reply_markup=btn)
    await state.finish()


async def payment_answer_callback_choose_buy(call: CallbackQuery):
    text = call.data.split(":")[-1]
    if text == 'click':
        keyboard = InlineKeyboardMarkup(row_width=1)
        btn = InlineKeyboardButton(text="💵 Tolov qilish 💵", url='click.uz/')
        keyboard.insert(btn)
        await call.message.answer("✅ Tolov qilish uchun pastdagi tugmani bosing", reply_markup=keyboard)
    if text == 'qiwi':
        keyboard = InlineKeyboardMarkup(row_width=1)
        btn = InlineKeyboardButton(text="💵 Tolov qilish 💵", url='qiwi.ru/')
        keyboard.insert(btn)
        await call.message.answer("✅ Tolov qilish uchun pastdagi tugmani bosing", reply_markup=keyboard)


def register_users_py(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])
    dp.register_message_handler(user_profile_handler, regexp='👤 Profil')
    dp.register_message_handler(add_plan_rate_handler, regexp='➕ A`zo bolish')

    dp.register_callback_query_handler(payment_answer_callback_choose_buy, text_contains='payment:')
    dp.register_callback_query_handler(click_choose_type_callback_handler, text_contains='tolov:',
                                       state=Save_plan.tarif_rate)
    dp.register_callback_query_handler(choose_plan_callback_handler, text_contains='plan:', state=Save_plan.tarif_name)
