from app.utils import *

class User:

    def __init__(self, id, username, password, email, biography, profile_picture,
                    birth_date, deleted=False, conected=False):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.biography = biography
        self.profile_picture = profile_picture
        self.birth_date = birth_date
        self.deleted = deleted
        self.conected = conected

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
        """
        method to login a user

            identifient(str): can be an email or a username depending on he methode value
            password(str): well... the password (must be hashed)
            methode(str): "email" or "username" to differencie bettween them
        """
        db = database.db_connection()
        cursor = db.cursor()

        if methode == "username":
            sql_query = "SELECT password FROM user WHERE username=?"
        elif methode == "email":
            sql_query = "SELECT password FROM user WHERE email=?"

        cursor.execute(sql_query, (identifient, ))
        row = cursor.fetchone()
        cursor.close()
        if row == None:
            raise ValueError("useranme or email inexistent")
        else:
            # I'm gonna change this part to add some security to the password
            if row[0] == password:
                print("authantication confirmed")
                # charging the user data and if the account is deleted we must change that
                user_data = User.search(identifient, by=methode, type_retrun="dict")
                return User( **user_data, conected=True)
            else:
                print("wait, you're an impostor")
                return False

    @classmethod
    def search(cls, identifient, by="id", type_retrun="object"):
        """
        method to search a user in our database

        parameters:
            identifient(str): can be an email or a username or the id depending on he "by" value
            password(str): well... the password (must be hashed)
            by(str): "email" or "username" or "id" to differencie bettween them, DEFAULT : "id".
            type_retrun(str): "object" or "dict" or "row" , represent what the unction is supposed to return ,
                can be an user object, a dict containing the different values or an sqlite row, DEFAULT : "object".
        """
        if by == "id":
            sql_query = "SELECT * FROM user WHERE id_user=?"
        elif by == "username":
            sql_query = "SELECT * FROM user WHERE username=?"
        elif by == "email":
            sql_query = "SELECT * FROM user WHERE email=?"

        db = database.db_connection()
        cursor = db.cursor()
        cursor.execute(sql_query, (identifient, ))
        row = cursor.fetchone()
        cursor.close()

        # we check what return type is expected...
        if type_retrun == "object":
            user_dict = User.__row_to_dict(row)
            return User(**user_dict)
        elif type_retrun == "dict":
            return User.__row_to_dict(row)
        elif type_retrun == "row":
            return row
        else:
            raise ValueError("type_retrun parameter must be: 'object' or 'dict' or 'row'")

    @classmethod
    def register(cls, **info_user):
        db = database.db_connection()
        cursor = db.cursor()

        #check the informaion given
        User.__check_informations(info_user)
        sql_query = "INSERT INTO user(username, password, email, biography, path_proile_picture, birth_date) VALUES(?, ?, ?, ?, ?, ?)"
        cursor.execute(sql_query, (info_user["username"], info_user["password"], info_user["email"],
                info_user["biography"], info_user["profile_picture"], info_user["birth_date"]))
        cursor.close()
        db.commit()

        # creating an object with the user data
        return User(User.__get_last_id(), info_user["username"], info_user["password"], info_user["email"],
                info_user["biography"], info_user["profile_picture"], info_user["birth_date"])

    @classmethod
    def __get_last_id(cls):
        """ rerurn the last ID """
        db = database.db_connection()
        cursor = db.cursor()
        sql_query = "SELECT max(id_user) FROM user"
        cursor.execute(sql_query)
        row = cursor.fetchone()
        cursor.close()
        return int(row[0])

    @classmethod
    def __row_to_dict(cls, row):
        return {
            "id" : int(row["id_user"]),
            "username" : row["username"],
            "password" : row["password"],
            "email" : row["email"],
            "biography" : row["biography"],
            "profile_picture" : row["path_proile_picture"],
            "birth_date" : str_to_date(row["birth_date"]),
            "deleted" : bool(row["deleted"])
        }

    @classmethod
    def __check_informations(cls, info_user):
        default_info = ["biography", "profile_picture", "birth_date"]

        if "username" not in info_user or "password" not in info_user or "email" not in info_user:
            raise ValueError("the username, password or the email are missing")
        else:
            for information in default_info:
                if information not in info_user:
                    info_user[information] = None
