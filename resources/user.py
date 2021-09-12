from os import curdir
import sqlite3
from sqlite3.dbapi2 import Cursor
from flask_restful import Resource,reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type=str,
    required=True,
    help="Required Field Username"
    )
    parser.add_argument('password',
    type=str,
    required=True,
    help="Required Field Password"
    )
    def post(self):
        data  = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message : ": "User already exist"}
        
        user = UserModel(data['username'],data['password'])
        user.save_to_db()

        """conn = sqlite3.connect('data.db')

        cur = conn.cursor()

        query = "insert into users values (NULL,?,?)"

        cur.execute(query,(data['username'],data['password']))

        conn.commit()
        conn.close()"""

        return {"message: ": "user created successfully"},201