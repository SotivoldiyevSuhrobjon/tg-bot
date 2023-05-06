from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


async def menu_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row("Profil", "A`zo bolish")
    return btn


async def rate_options_btn():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton(text='Oy', callback_data='rate:Oy'),
        InlineKeyboardButton(text='Yil', callback_data='rate:Yil')
    )
    return btn