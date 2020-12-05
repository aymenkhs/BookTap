import sqlite3

DATABASE = 'my_db.db'

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
    except sqlite3.error as e:
        print(e)
    conn.row_factory = sqlite3.Row
    return conn
