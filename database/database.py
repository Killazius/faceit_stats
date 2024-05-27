import sqlite3


class BotDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def add_user(self, telegram_id, nickname):
        self.cursor.execute("INSERT OR REPLACE INTO users (telegram_id, nickname) VALUES (?, ?)",
                            (telegram_id, nickname))
        return self.conn.commit()

    def find_nickname_by_telegram_id(self, telegram_id):
        self.cursor.execute("SELECT nickname FROM users WHERE telegram_id = ?", (telegram_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
    def user_exists(self, telegram_id):
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `telegram_id` = ?", (telegram_id,))
        return bool(len(result.fetchall()))
