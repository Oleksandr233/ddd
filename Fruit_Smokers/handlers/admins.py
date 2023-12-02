from aiogram.types import CallbackQuery
from sqlite_db import DataBase
from aiogram import Router

router3 = Router()


@router3.callback_query()
async def call_adm_panel(call: CallbackQuery) -> None:
    if call.data == 'send_news':
        db = DataBase()
        user_id = call.from_user.id

        if db.users_exist(user_id):
            text = call.message.text
            # Assuming you want to send the message back to the admin
            await call.message.answer(f"User {user_id} exists. Message: {text}")
        else:
            await call.message.answer(f"User {user_id} does not exist.")
