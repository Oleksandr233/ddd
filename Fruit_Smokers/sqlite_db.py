import sqlite3


# Функция для добавления нового пользователя в базу данных
def add_user(cursor, user_id, username):
    cursor.execute('''INSERT OR IGNORE INTO users (user_id, username, admin) VALUES (?, ?, ?)''', (user_id, username, False))


# Создаем таблицу для хранения ID пользователей
def setup_database(database_file):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT, admin BOOLEAN)''')
    conn.commit()
    return conn, cursor


# Проверка на админа
def is_admin(cursor, user_id):
    cursor.execute('''SELECT admin FROM users WHERE user_id = ?''', (user_id,))
    result = cursor.fetchone()
    if result:
        return bool(result[0])
    return False


class DataBase:
    def __init__(self, db_path='user_ids.db') -> None:
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def users_exist(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,)).fetchone()
            return bool(result)
