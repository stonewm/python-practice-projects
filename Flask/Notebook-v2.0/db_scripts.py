
from app.models import db
from app import create_app

app = create_app()
db.app = app
db.init_app(app)

if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # print ('Done')