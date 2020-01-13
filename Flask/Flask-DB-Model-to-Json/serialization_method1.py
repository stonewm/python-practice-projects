from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from collections import OrderedDict


app = Flask(__name__)

# app.configurations
app.config['SECURITY_KEY'] = 'you will never guess'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'

    USER_ID = db.Column(db.Integer, primary_key=True)
    USERNAME = db.Column(db.String(20))
    CREATED_BY = db.Column(db.String(20))
    CREATED_DATE = db.Column(db.Date)


def user_to_dict(user):
    return OrderedDict(
        USER_ID = user.USER_ID,
        USERNAME = user.USERNAME,
        CREATED_BY = user.CREATED_BY,
        CREATED_DATE = user.CREATED_DATE
    )


@app.route('/users')
def list_users():
    users = User.query.all()
    return jsonify(list(map(user_to_dict, users)))

@app.route('/users/<userid>')
def find_user(userid):
    user = User.query.get(userid)
    return jsonify(user_to_dict(user))


if __name__ == "__main__":
    app.run(debug=True)
