from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def rate_verify_btn():
    btn = InlineKeyboardMarkup(row_width=1)
    btn.add(
        InlineKeyboardButton("Tasdiqlash", callback_data="save:verify"),
        InlineKeyboardButton("❌ Bekor qilish", callback_data="save:delete")
    )
    return btn


async def delete_rate_btn(data):
    btn = InlineKeyboardMarkup(row_width=1)
    btn.add(
        *[InlineKeyboardButton(f"{item['tariff']['name']} : {item['period']}", callback_data=f"delete:{item['id']}") for item in data]
    )
    return btn
