from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def choose_plan_menu_btn(tarif):
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        *[InlineKeyboardButton(f"{data}", callback_data=f"plan:{data}") for data in tarif]
    )
    return btn


async def inline_choose_plan(tarif):
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        *[InlineKeyboardButton(f"{data}", callback_data=f"tolov:{data}") for data in tarif]

    )
    return btn


async def inline_choose_payment():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton("Qiwi", callback_data=f"payment:qiwi"),
        InlineKeyboardButton("Click", callback_data=f"payment:click"),
    )
    return btn
