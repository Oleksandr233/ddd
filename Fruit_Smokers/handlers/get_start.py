from aiogram import Router
from aiogram.types import Message
from keyboards import Inline_button
from aiogram.filters import CommandStart
from sqlite_db import add_user, setup_database, is_admin
from text import text

# Инициализируем Роутер
router1 = Router()

# Инициализация базы данных
conn, cursor = setup_database('user_ids.db')


@router1.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Этот обработчик обрабатывает команду '/start'
    """
    username = message.from_user.full_name
    user_id = message.from_user.id

    # Добавляем пользователя в базу данных
    add_user(cursor, user_id, username)
    conn.commit()

    # Проверка на админа и отправка текста и клавиатуры
    if is_admin(cursor, user_id):
        await message.answer(text.start_admin_txt, reply_markup=Inline_button.start_admin_bot_kb())
    else:
        await message.answer(text.start_txt, reply_markup=Inline_button.start_bot_kb())

    conn.commit()
