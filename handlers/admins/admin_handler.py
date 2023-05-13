from asyncio import sleep

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import *

from data.config import ADMINS
from database.connections import *
from keyboards.default.admin_menu_btn import admin_add_rate_btn, rate_and_price_btn, cancel_btn, remove
from keyboards.default.users_menu import *
from keyboards.inline.verify_btn_admin import rate_verify_btn, delete_rate_btn
from loader import dp
from states.AllStates import Rate_state


# admin start handler
async def admin_start(msg: Message):
    user_id = msg.from_user.id
    if user_id in ADMINS:
        btn = await admin_add_rate_btn()
        await msg.answer(f"✅ siz admin paneldasiz ✅", reply_markup=btn)


# 1: state add rate/tarif name handler
async def add_rate_name_handler(msg: Message, state: FSMContext):
    btn = await cancel_btn()
    await msg.answer("♻️ iltimos tarif nomini kiriting", reply_markup=btn)
    await Rate_state.name.set()


# 2: rate name save
# state choose month/year handler
async def choose_month_year_handler(msg: Message, state: FSMContext):
    text = msg.text
    if text == 'Bekor qilish':
        btn = await admin_add_rate_btn()
        await msg.answer("Bekor qilindi")
        await call.message.answer(f"✅ siz admin paneldasiz ✅", reply_markup=btn)
        await state.finish()
    else:
        await state.update_data(name=text)
        btn = await rate_options_btn()
        await msg.answer("🖌 Iltimos tugmani tanlang", reply_markup=btn)
        await Rate_state.oy.set()


# 3:  choose month/year save
# state choose month 1 and year 2 handler
async def choose_term_callback_handler(call: CallbackQuery, state: FSMContext):
    await call.answer()
    text = call.data.split(":")[-1]
    s = await state.get_data()
    await state.update_data(period=text)
    if text == 'oy' and 'oy' not in s.keys():
        await state.update_data({'oy': []})
    elif text == 'yil' and 'yil' not in s.keys():
        await state.update_data({'yil': []})
    btn = await cancel_btn()
    await call.message.answer(f"🕐 Siz <b>{text}</b>  ni tanladingiz Iltimos muddatini kiriting raqamlarda", reply_markup=btn)
    await Rate_state.muddat.set()


# 5: oy save
# state narx handler
async def add_price_handler(msg: Message, state: FSMContext):
    muddat = msg.text
    if muddat == 'Bekor qilish':
        btn = await admin_add_rate_btn()
        await msg.answer("✅ Bekor qilindi")
        await msg.answer(f"siz admin paneldasiz", reply_markup=btn)
        await state.finish()
    else:
        async with state.proxy() as data:
            if data['period'] == 'oy':
                data['oy'].append([muddat])
            else:
                data['yil'].append([muddat])
        await msg.answer("💵 Iltimos narxni kiriting so'mda ")
        await Rate_state.narx.set()


# 6: narx save
# state add muddat, cancel, continue handler
async def all_save_rate(msg: Message, state: FSMContext):
    narx = msg.text
    if narx == 'Bekor qilish':
        btn = await admin_add_rate_btn()
        await msg.answer("Bekor qilindi")
        await msg.answer(f"✅ siz admin paneldasiz ✅", reply_markup=btn)
        await state.finish()
    else:
        async with state.proxy() as data:
            if data['period'] == 'oy':
                data['oy'][-1].append(narx)
            elif data['period'] == 'yil':
                data['yil'][-1].append(narx)
        await state.reset_state(with_data=False)
        btn = await rate_and_price_btn()
        await msg.answer("✅ Iltimos tugmalardan birini tanlang", reply_markup=btn)
        await Rate_state.choose.set()


async def choose_add_term_handler(msg: Message, state: FSMContext):
    text = msg.text
    if text == 'Yana muddat kiritish':
        btn = await rate_options_btn()
        await msg.answer("🖌 Iltimos tugmani tanlang", reply_markup=btn)
        await Rate_state.oy.set()
    elif text == 'Bekor qilish':
        btn = await admin_add_rate_btn()
        await msg.answer("Bekor qilindi")
        await msg.answer(f"✅ siz admin paneldasiz ✅", reply_markup=btn)

        await state.finish()
    elif text == 'Davom etish':
        async with state.proxy() as data:
            context = ''
            context1 = ''
            if 'oy' in data.keys():
                for item1 in data['oy']:
                    context1 += f"{item1[0]} oy: {item1[1]} so`m"
            if 'yil' in data.keys():
                for item in data['yil']:
                    context += f"{item[0]} yil: {item[1]} so`m"
            else:
                pass
            btn = await rate_verify_btn()

            await msg.answer(f"name: {data['name']}\n\n"
                             f'{context}\n\n'
                             f"{context1}\n\n", reply_markup=btn)
        await Rate_state.save.set()


async def verify_state_save_callback_handler(call: CallbackQuery, state: FSMContext):
    text = call.data.split(":")
    if 'verify' in text:
        data = await state.get_data()
        await call.answer("Saqlandi")
        await call.message.delete()
        btn = await admin_add_rate_btn()
        await call.message.answer(f"✅ siz admin paneldasiz ✅", reply_markup=btn)
        await get_add_tarif_name(
            name=f"{data['name']}",
        )
        await get_add_tariff_period(data)
    if 'delete' in text:
        await call.answer("Bekor qilindi")
        await call.message.delete()
        await state.finish()
        btn = await admin_add_rate_btn()
        await call.message.answer(f"✅ siz admin paneldasiz ✅", reply_markup=btn)
    await state.reset_state()


async def delete_plan_handler(msg: Message):
    tariff_period = await get_tariff_period_delete()
    btn = await delete_rate_btn(tariff_period)
    await msg.answer("❌ Ochiriladigan tarifni tanlang", reply_markup=btn)


@dp.callback_query_handler(text_contains='delete:')
async def delete_user_callback(call: CallbackQuery):
    user_id = call.data.split(':')[-1]
    await delete_tariff_period(user_id)
    await call.answer(f"{user_id} deleted!")
    await call.message.delete()
    await delete_plan_handler(call.message)


def admin_register_py(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=['admin'])
    dp.register_message_handler(add_rate_name_handler, text=['Tarif qoshish'])

    dp.register_message_handler(add_price_handler, state=Rate_state.muddat)
    dp.register_message_handler(choose_month_year_handler, state=Rate_state.name)
    dp.register_message_handler(choose_add_term_handler, state=Rate_state.choose)
    dp.register_message_handler(all_save_rate, state=Rate_state.narx)
    dp.register_callback_query_handler(choose_term_callback_handler, state=Rate_state.oy, text_contains='rate:')
    dp.register_callback_query_handler(verify_state_save_callback_handler, state=Rate_state.save,
                                       text_contains='save:')

    dp.register_message_handler(delete_plan_handler, text=['Tarif ochirish'])
