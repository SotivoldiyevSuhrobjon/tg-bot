# import types
# from aiogram import Bot, Dispatcher, types
# from aiogram.types import *
#
# from keyboards.default.users_menu import bot_link
# from loader import bot
#
#
# # from aiogram.types.chat import ChatType
#
#
# async def group_user_start_handler(msg: Message):
#     if msg.chat.type == types.ChatType.SUPERGROUP:
#         group_count =
#         text = msg.text
#         fullname = msg.from_user.full_name
#         user_id = msg.from_user.id
#         btn = await bot_link()
#         await msg.delete()
#         await msg.answer(text=f"<a href='tg://user?id={user_id}' >{fullname}</a> "
#                               f"Iltimos bot lichkasiga yozing va tarifni tanlang aks xolda 24-soatda guruhdan chiqarib yuborilasiz",
#                          reply_markup=btn)
#
#
# def group_register_py(dp: Dispatcher):
#     dp.register_message_handler(group_user_start_handler, content_types=['text'])
