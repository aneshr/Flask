import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users' # for SQL Alchemy to know about table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(15))

    def __init__(self, username, password):
        #self.id = _id
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(self, username):
        return UserModel.query.filter_by(username=username).first()
        """conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query = "SELECT * FROM users WHERE username=?"

        result = cur.execute(query,(username,))  #parameter should be in form of a tuple
        row = result.fetchone()

        if row:
            user = UserModel(*row) # Better way of calling the constructor, can be used if using decorator.
            #user = User(row[0],row[1],row[2])
        else:
            user = None

        conn.close()
        return user"""

    @classmethod
    def find_by_id(self, _id):
        return UserModel.query.filter_by(id=_id).first()
        """conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query = "SELECT * FROM users WHERE id=?"

        result = cur.execute(query,(_id,))  #parameter should be in form of a tuple
        row = result.fetchone()

        if row:
            user = UserModel(*row) # Better way of calling the constructor, can be used if using decorator.
            #user = User(row[0],row[1],row[2])
        else:
            user = None

        conn.close()
        return user"""