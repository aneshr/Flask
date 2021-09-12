#implementing authentication in FLask
from resources.user import UserModel
'''
users = [
    User(1,'aneshr','something')
]

username_mapping = {{
    'aneshr': {
        'id': 1,
        'username': 'aneshr',
        'password': 'something'
    }
}}

userid_mapping = {
    1:{
        'id': 1,
        'username': 'aneshr',
        'password': 'something'
    }
}
username_mapping = {u.username: u for u in users}

userid_mapping = {u.id: u for u in users}
#authenticate a user
'''

def authenticate(username,password):
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)



