from flask import Blueprint

adminbp = Blueprint('adminbp', __name__, url_prefix='/admin')

@adminbp.route('/')
def index():
    return 'Admin blueprint, index page'