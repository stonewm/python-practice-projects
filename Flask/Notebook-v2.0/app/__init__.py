
from flask import Flask
import configs
from app.models import db
from app.views import notesbp
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)

    # 配置
    app.config.from_object(configs)

    # 初始化db
    db.app = app
    db.init_app(app)

    # 注册蓝图
    app.register_blueprint(notesbp)

    Bootstrap(app=app)

    return app
