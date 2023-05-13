from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def choose_plan_menu_btn(tarif):
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        *[InlineKeyboardButton(f"{data[0]}", callback_data=f"plan:{data[0]}/{data[-1]}") for data in tarif]
    )
    return btn


async def inline_choose_plan(plan):
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        *[InlineKeyboardButton(f"{item[0][0:]}  {item[-1]} so'm", callback_data=f"tolov:{item[0][0:]}/{item[-1]}") for item in plan]

    )
    return btn


async def inline_choose_payment():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton("Qiwi", callback_data=f"payment:qiwi"),
        InlineKeyboardButton("Click", callback_data=f"payment:click"),
    )
    return btn

