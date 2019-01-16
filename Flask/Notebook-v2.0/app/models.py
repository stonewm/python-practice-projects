
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body = db.Column(db.Text)

    def __repr__(self):
        return 'Note body: {}'.format(self.body)

