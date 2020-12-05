from app.utils import *


class Author:
    def __init__(self, id_author, name_author, birth_date, death_date, biography):
        self.id_author = id_author
        self.name_author = name_author
        self.birth_date = birth_date
        self.death_date = death_date
        self.biography = biography

    def delete(cls, id_author):
        pass

    def update(cls, id_book, **info_author):
        pass

    @classmethod
    def create(cls, **info_author):
        db = database.db_connection()
        cursor = db.cursor()

        #check the informaion given
        Author.__check_informations(info_author)

        sql_query = "INSERT INTO author(author_lastname, author_firstname, birth_date, death_date, biography, path_picture) VALUES(?, ?, ?, ?, ?, ?)"
        cursor.execute(sql_query, (info_author["last_name"], info_author["first_name"], info_author["birth_date"],
                info_author["death_date"], info_author["biography"], info_author["path_picture"]))

        # creating an object with the author data
        cursor.close()
        db.commit()

    @classmethod
    def search(cls, **info_author):
        pass

    @classmethod
    def search_by_id(cls, id):
        db = database.db_connection()
        cursor = db.cursor()

        sql_query = "SELECT * FROM author where id_author=?"
        cursor.execute(sql_query, (id))
        row = cursor.fetchone()

        if row == None:
            raise ValueError("author non existent")
        else:
            # charge the author and return it
            print(row)
        cursor.close()

    @classmethod
    def return_all_authors(cls):
        db = database.db_connection()
        cursor = db.cursor()
        sql_query = "SELECT * FROM author"
        cursor.execute(sql_query)
        row = cursor.fetchall()
        return row
        # charging each author as an object in a list and returning it

    @classmethod
    def __check_informations(cls, info_author):
        default_info = ["birth_date", "death_date", "biography", "path_picture"]

        if "last_name" not in info_author or "first_name" not in info_author:
            raise ValueError("the last name or the first name of the author are missing")
        else:
            for information in default_info:
                if information not in info_author:
                    info_author[information] = None
