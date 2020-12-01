from app import database

def select(table, val="*", by="id"):
    db = database.db_connection()
    cursor = db.cursor()

    cursor.close()

def insert(table, **values):
    db = database.db_connection()
    cursor = db.cursor()

    cursor.close()

def modify(table, to_modify, by="id", **values):
    db = database.db_connection()
    cursor = db.cursor()

    cursor.close()
