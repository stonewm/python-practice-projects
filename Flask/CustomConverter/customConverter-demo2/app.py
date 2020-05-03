from flask import Flask, jsonify, url_for
from ListConverter import ListConverter

app = Flask(__name__)
app.url_map.converters['list'] = ListConverter


@app.route('/')
def index():
    print(url_for('greet_user', users=[1, 4, 6]))
    return 'Home Page'


@app.route('/users/<list:users>')
def greet_user(users):
    names = ','.join(user for user in users)
    return 'Hello: ' + names


if __name__ == "__main__":
    app.run()
