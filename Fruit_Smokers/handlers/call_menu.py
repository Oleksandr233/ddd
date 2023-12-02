from keyboards.Inline_button import admin_kb, help_kb, towns_kb
from aiogram.types import CallbackQuery
from text import text
from aiogram import Router

# Инициализируем Роутер
router2 = Router()


# Обработчик коллбеков
@router2.callback_query()
async def call_menu(call: CallbackQuery) -> None:
    """
    эта функция ловит коллбеки с меню
    """

    # Если нажал на кнопку 🌆 Города
    if call.data == "cities":
        await call.message.answer(text.towns_txt, reply_markup=towns_kb())

    # Если нажал на кнопку ❓ Справка
    elif call.data == "help":
        await call.message.answer(text.help_txt, reply_markup=help_kb())

    # Если нажал на кнопку 🔒 Админ панель
    elif call.data == "Admin_kb":
        await call.message.answer(text.admin_panel_txt, reply_markup=admin_kb())
