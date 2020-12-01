


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
    def log_in(cls, id):
        pass

    @classmethod
    def register(cls, username, password, email, biography, profile_picture,
                    birth_date, deleted):
        self.id = User.get_total_users() + 1

    @classmethod
    def get_total_users(cls):
        pass

class Comment:
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
