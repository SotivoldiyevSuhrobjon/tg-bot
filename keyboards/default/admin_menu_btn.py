from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


async def admin_add_rate_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row("Tarif qoshish")
    return btn


async def rate_verify_btn():
    btn = InlineKeyboardMarkup(row_width=1)
    btn.add(
        InlineKeyboardButton("Tasdiqlash", callback_data="rate:verify"),
        InlineKeyboardButton("❌ Bekor qilish", callback_data="rate:delete")
    )
    return btn
