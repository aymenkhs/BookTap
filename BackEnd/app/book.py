from app.utils import *

class Book:
    def __init__(self, id_book, book_name, categorie, global_grade, editor, release_year,
                    nb_pages, abstract, cover_page):
        self.id_book = id_book
        self.book_name = book_name
        self.category = category
        self.global_grade = global_grade
        self.editor = editor
        self.release_year = release_year
        self.nb_pages = nb_pages
        self.cover_page = cover_page
        self.abstract = abstract

    def delete(cls, id_book):
        pass

    def update(cls, id_book, **info_book):
        pass

    @classmethod
    def create(cls, **info_book):
        db = database.db_connection()
        cursor = db.cursor()

        #check the informaion given
        Book.__check_informations(info_book)

        if "id_author" in info_book:
            # searching if the author exist
            sql_query = "INSERT INTO book(book_name, category, global_grade, editor, abstract, nb_pages, path_cover_page, release_year, id_author) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(sql_query, (info_book["book_name"], info_book["category"], info_book["global_grade"],
                info_book["editor"], info_book["abstract"], info_book["nb_pages"], info_book["path_cover_page"],
                        info_book["release_year"], info_book["id_author"]))
        elif "author" in info_book:
            # finding the id_author
            sql_query = "INSERT INTO book(book_name, category, global_grade, editor, abstract, nb_pages, path_cover_page, release_year, id_author) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(sql_query, (info_book["book_name"], info_book["category"], info_book["global_grade"],
                info_book["editor"], info_book["abstract"], info_book["nb_pages"], info_book["path_cover_page"],
                        info_book["release_year"], info_book["id_author"]))
        else:
            sql_query = "INSERT INTO book(book_name, category, global_grade, editor, abstract, nb_pages, path_cover_page, release_year) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(sql_query, (info_book["book_name"], info_book["category"], info_book["global_grade"],
                info_book["editor"], info_book["abstract"], info_book["nb_pages"], info_book["path_cover_page"],
                                            info_book["release_year"]))
        # creating an object with the book data
        cursor.close()
        db.commit()

    @classmethod
    def search(cls, **info_book):
        pass

    @classmethod
    def search_by_id(cls, id):
        db = database.db_connection()
        cursor = db.cursor()

        sql_query = "SELECT * FROM book where id_book=?"
        cursor.execute(sql_query, (id))
        row = cursor.fetchone()

        if row == None:
            raise ValueError("book non existent")
        else:
            # charge the book and return it
            print(row)

        cursor.close()

    @classmethod
    def return_all_books(cls):
        db = database.db_connection()
        cursor = db.cursor()
        sql_query = "SELECT * FROM book"
        cursor.execute(sql_query)
        row = cursor.fetchall()
        return row
        # charging each book as an object in a list and returning it

    @classmethod
    def __check_informations(cls, info_book):
        default_info = ["global_grade", "editor", "abstract", "nb_pages", "path_cover_page", "release_year"]

        if "book_name" not in info_book or "category" not in info_book:
            raise ValueError("the book name or the category are missing")
        else:
            for information in default_info:
                if information not in info_book:
                    info_book[information] = None
