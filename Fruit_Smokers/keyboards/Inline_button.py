from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_admin_bot_kb():
    """
    Кнопки при старте для админа
    """
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🌆 Города', callback_data='cities')
    keyboard_builder.button(text='❓ Справка', callback_data='help')
    keyboard_builder.button(text='🔒 Админ панель', callback_data='Admin_kb')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()


def start_bot_kb():
    """
    Кнопки при старте для пользователя
    """
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🌆 Города', callback_data='cities')
    keyboard_builder.button(text='❓ Справка', callback_data='help')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()


def admin_kb():
    """
    Кнопки при нажатии на 🔒 Админ панель
    """
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='📣 Рассылка', callback_data="send_news")
    keyboard_builder.button(text="➕ Добавить товар", callback_data="add_product")
    keyboard_builder.button(text='🗑️ Удалить товар', callback_data="delete_product")
    keyboard_builder.button(text='✏️ Изменить описание', callback_data="edit_description")
    keyboard_builder.button(text='⬅️ Главное меню', callback_data='main_menu')
    keyboard_builder.adjust(1, 2, 1, 1)
    return keyboard_builder.as_markup()


def towns_kb():
    """
    Кнопки при нажатии на 🌆 Города
    """
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🏰 Erlangen', callback_data='Erlangen')
    keyboard_builder.button(text='🌆 Nürnberg', callback_data='Nürnberg')
    keyboard_builder.button(text='🏡 Fürth', callback_data='Fürt')
    keyboard_builder.button(text='🌇 Köln', callback_data='Köln')
    keyboard_builder.button(text='⬅️ В главное меню', callback_data='menu')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()


def help_kb():
    """
    Кнопки при нажатии на ❓ Справка
    """
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🛒 Покупка', callback_data='shop')
    keyboard_builder.button(text='🔄 Возврат', callback_data='back')
    keyboard_builder.button(text='▪️ Другое', callback_data='info')
    keyboard_builder.button(text='⬅️ В главное меню', callback_data='menu')
    keyboard_builder.adjust(2, 1, 1)
    return keyboard_builder.as_markup()


def shop_kb():
    """
    Кнопки при нажатии на 🛒 Покупка
    """
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='💡 Предложить', url='https://t.me/fruitsmokers')
    keyboard_builder.button(text='↩️ Назад', callback_data='Spravka')
    keyboard_builder.button(text='⬅️ В главное меню', callback_data='menu')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()


def return_kb():
    """
    Кнопки при нажатии на 🔄 Возврат
    """
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🔄 Хочу вернуть', url='https://t.me/fruitsmokers')
    keyboard_builder.button(text='↩️ Назад', callback_data='Spravka')
    keyboard_builder.button(text='⬅️ В главное меню', callback_data='menu')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()


def info_kb_other():
    """
    Кнопки при нажатии на ▪️ Другое
    """
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='✏️ Написать', url='https://t.me/fruitsmokers')
    keyboard_builder.button(text='↩️ Назад', callback_data='Spravka')
    keyboard_builder.button(text='⬅️ В главное меню', callback_data='menu')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()
