from flask import Flask, url_for
from user import userbp
from admin import adminbp

app = Flask(__name__)


def index():
    print(url_for('index'))
    return 'Index Page'


def about():
    return 'About Page'


if __name__ == '__main__':
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/about', endpoint='about', view_func=about)
    print(app.url_map)
    app.run()
