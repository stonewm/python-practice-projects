from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

# application configurations
app.config['SECURITY_KEY'] = 'you will never guess'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    __tablename__ = 'user'

    USER_ID = db.Column(db.Integer, primary_key=True)
    USERNAME = db.Column(db.String(20), nullable=False)
    CREATED_BY = db.Column(db.String(20), nullable=False)
    CREATED_DATE = db.Column(db.Date, nullable=False)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


@app.route('/users')
def list_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)

    user_data = user_schema.dump(users).data

    return jsonify(user_data)


@app.route('/users/<userid>')
def find_user(userid):
    user = User.query.get(userid)
    user_schema = UserSchema()

    user_data = user_schema.dump(user).data

    return jsonify(user_data)


if __name__ == "__main__":
    app.run(debug=True)
