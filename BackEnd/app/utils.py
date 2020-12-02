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
        id = User.get_total_users() + 1
        sql_query = "INSERT INTO user(id_user, username, password, email, biography, path_proile_picture, birth_date) VALUES(?, ?, ?, ?, ?, ?, ?)"
        print(sql_query)
        cursor.execute(sql_query, (id, username, password, email, biography, profile_picture, birth_date))
        # creating an object with the user data
        cursor.close()
        db.commit()

    @classmethod
    def get_total_users(cls):
        return 0

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

    @classmethod
    def create(cls, **info_comment):
        pass

    @classmethod
    def update(cls, id_comment, new_content):
        pass

    @classmethod
    def search(cls, id_comment):
        pass

    @classmethod
    def delete(cls, id_comment):
        pass

    @classmethod
    def get_total_comments(cls):
        pass

class Book:
    def __init__(self, id_book, book_name, categorie, global_grade, editor, release_year,
                    nb_pages, abstract, cover_page):
        self.id_book = id_book
        self.book_name = book_name
        self.categorie = categorie
        self.global_grade = global_grade
        self.editor = editor
        self.release_year = release_year
        self.nb_pages = nb_pages
        self.cover_page = cover_page
        self.abstract = abstract

    @classmethod
    def create(cls, **info_book):
        pass

    @classmethod
    def update(cls, id_book, **info_book):
        pass

    @classmethod
    def search(cls, **info_book):
        pass

    @classmethod
    def delete(cls, id_book):
        pass

    @classmethod
    def return_all_books(cls, **info_book):
        pass

    @classmethod
    def get_total_books(cls):
        pass

class Author:
    def __init__(self, id_author, name_author, birth_date, death_date, biography):
        self.id_author = id_author
        self.name_author = name_author
        self.birth_date = birth_date
        self.death_date = death_date
        self.biography = biography

    @classmethod
    def create(cls, **info_author):
        pass

    @classmethod
    def update(cls, id_book, **info_author):
        pass

    @classmethod
    def search(cls, **info_author):
        pass

    @classmethod
    def delete(cls, id_author):
        pass

    @classmethod
    def return_all_authors(cls, **info_author):
        pass

    @classmethod
    def get_total_authors(cls):
        pass
