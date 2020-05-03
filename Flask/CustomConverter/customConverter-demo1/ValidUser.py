from werkzeug.routing import BaseConverter, ValidationError

_users = [
    {'id': '1', 'username': 'Admin'},
    {'id': '2', 'username': 'Stone'}
]

def find_user(userid):
    for user in _users:
        if userid == user['id']:
            return user

class ValidUserConverter(BaseConverter):
    
    def to_python(self, value):
        if not find_user(value) is None:
            return find_user(value)['username']
        raise ValidationError()
