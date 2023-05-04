from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def inline_choose_plan():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton("1 Oylik", callback_data=f"tolov:oylik"),
        InlineKeyboardButton("1 Yillik", callback_data=f"tolov:yilllik"),
    )
    return btn


async def inline_choose_payment():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton("Qiwi", callback_data=f"tolov:qiwi"),
        InlineKeyboardButton("Click", callback_data=f"tolov:click"),
    )
    return btn