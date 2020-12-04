from flask import Flask, jsonify, url_for
from ValidUser import ValidUserConverter

app = Flask(__name__)
app.url_map.converters['validuser'] = ValidUserConverter

@app.route('/')
def index():
    return 'Home Page'

@app.route('/users/<validuser:userid>')
def greet_user(userid):
    print(url_for('greet_user', userid='1'))
    return jsonify({'Hello': userid})


if __name__ == "__main__":
    app.run()