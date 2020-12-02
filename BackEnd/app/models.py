from app import database

def select(table, val="*", by="id"):
    db = database.db_connection()
    cursor = db.cursor()

    cursor.close()

def insert(table, **values):
    db = database.db_connection()
    with closing(db.cursor()) as cursor:
        pass

def modify(table, to_modify, by="id", **values):
    db = database.db_connection()
    cursor = db.cursor()

    cursor.close()
