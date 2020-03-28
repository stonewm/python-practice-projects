from flask import Flask, url_for
from user import userbp
from admin import adminbp

app = Flask(__name__)
app.register_blueprint(userbp)
app.register_blueprint(adminbp)


@app.route('/', endpoint='index')
def index():
    return 'Index Page'


if __name__ == '__main__':
    print(app.url_map)
    app.run()
