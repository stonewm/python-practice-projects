from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from collections import OrderedDict


app = Flask(__name__)

# application configurations
app.config['SECURITY_KEY'] = 'you will never guess'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)

class EntityBase(object):
    def to_json(self):
        fields = self.__dict__
        if "_sa_instance_state" in fields:
            del fields["_sa_instance_state"]
        
        return fields

class User(db.Model, EntityBase):
    __tablename__ = 'user'

    USER_ID = db.Column(db.Integer, primary_key=True)
    USERNAME = db.Column(db.String(20))
    CREATED_BY = db.Column(db.String(20))
    CREATED_DATE = db.Column(db.Date)


@app.route('/users')
def list_users():
    users = User.query.all()
    users_output = []
    for user in users:
        users_output.append(user.to_json())
    return jsonify(users_output)


@app.route('/users/<userid>')
def find_user(userid):
    user = User.query.get(userid)
    return jsonify(user.to_json())


if __name__ == "__main__":
    app.run(debug=True)
