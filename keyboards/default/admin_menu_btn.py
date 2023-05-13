from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

remove = ReplyKeyboardRemove()


async def admin_add_rate_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row("Tarif qoshish", "Tarif ochirish")
    return btn


async def rate_and_price_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.row("Yana muddat kiritish", "Davom etish"),
    btn.row("Bekor qilish"),
    return btn


async def cancel_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.row("Bekor qilish"),
    return btn
