
from flask_login import UserMixin

class User(UserMixin):
    pass

users = [
    {'id':'Tom', 'username': 'Tom', 'password': '111111'},
    {'id':'Michael', 'username': 'Michael', 'password': '123456'}
]

def query_user(id):
    for user in users:
        if id == user['id']:
            return user