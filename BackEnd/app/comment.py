from app.utils import *


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
