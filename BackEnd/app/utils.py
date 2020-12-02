from app import database


class User:

    def __init__(self, id, username, password, email, biography, profile_picture,
                    birth_date, deleted):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.biography = biography
        self.profile_picture = profile_picture
        self.birth_date = birth_date
        self.deleted = deleted

    def like(self, book):
        pass

    def dislike(self, book):
        pass

    def give_grade(self, book, grade):
        pass

    def remove_grade(self, book):
        pass

    def comment(self, comment):
        pass

    def remove_comment(self, comment):
        pass

    def upvote(self, comment):
        pass

    def downvote(self, comment):
        pass

    @classmethod
    def login(cls, identifient, password, methode="username"):
        db = database.db_connection()
        cursor = db.cursor()

        if methode == "username":
            sql_query = "SELECT password FROM user WHERE username=?"
        elif methode == "email":
            sql_query = "SELECT password FROM user WHERE email=?"

        cursor.execute(sql_query, (identifient, ))
        row = cursor.fetchone()
        if row == None:
            raise ValueError("useranme or email inexistent")
        else:
            # I'm gonna change this part to add some security to the password
            if row[0] == password:
                print("authantication confirmed")
                # charging the user data
                return True
            else:
                print("wait, you're an impostor")
                return False
        cursor.close()


    @classmethod
    def register(cls, username, password, email, biography, profile_picture,
                    birth_date):
        db = database.db_connection()
        cursor = db.cursor()

        #check the informaion given
        sql_query = "INSERT INTO user(username, password, email, biography, path_proile_picture, birth_date) VALUES(?, ?, ?, ?, ?, ?)"
        print(sql_query)
        cursor.execute(sql_query, (username, password, email, biography, profile_picture, birth_date))
        # creating an object with the user data
        cursor.close()
        db.commit()


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
        Book.__check_informations(info_author)

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
    def return_all_authors(cls, **info_author):
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

        if "last_name" not in info_book or "first_name" not in info_book:
            raise ValueError("the last name or the first name of the author are missing")
        else:
            for information in default_info:
                if information not in info_book:
                    info_book[information] = None


class Comment:
    def __init__(self, id_comment, book, user, content, deleted, upvotes, downvotes,
                            replies):
        self.id_comment = id_comment
        self.book = book
        self.user = user
        self.content = content
        self.deleted = deleted
        self.upvotes = upvotes
        self.downvotes = downvotes
        self.replies = replies

    def delete(cls, id_comment):
        pass

    def update(cls, id_comment, new_content):
        pass

    @classmethod
    def create(cls, user, book, content, parent=None):
        """ create a comment, add it to the database retrun a comment"""
        pass

    @classmethod
    def search(cls, id_comment):
        """ search a single comment with his ID, return a comment """
        db = database.db_connection()
        cursor = db.cursor()

        sql_query = "SELECT * FROM comment where id_comment=?"
        cursor.execute(sql_query, (id))
        row = cursor.fetchone()

        if row == None:
            raise ValueError("comment non existent")
        else:
            # charge the comment and return it
            print(row)
        cursor.close()

    @classmethod
    def search_by_user(cls, user):
        """ search comments by a particular user, return a list of comments """
        db = database.db_connection()
        cursor = db.cursor()
        sql_query = "SELECT * FROM comment where id_user=?"
        cursor.execute(sql_query, (user.id))
        row = cursor.fetchall()
        # charge the comments and add them to a list and return them
        print(row)
        cursor.close()

    @classmethod
    def search_by_book(cls, book):
        """ search comments by a particular book, return a set of comments """
        db = database.db_connection()
        cursor = db.cursor()
        sql_query = "SELECT * FROM comment where id_book=?"
        cursor.execute(sql_query, (book.id_book))
        row = cursor.fetchall()
        # charge the comments and add them to a tree and return them
        print(row)
        cursor.close()
