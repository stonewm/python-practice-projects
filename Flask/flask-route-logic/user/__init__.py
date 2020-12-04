from flask import Blueprint

userbp = Blueprint('userbp', __name__, url_prefix='/user')

@userbp.route('/')
def index():
    return 'User blueprint, index page'