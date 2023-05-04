from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def menu_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row("Profil", "A`zo bolish")
    return btn
