from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    from .views import views
    from .auth import auth
    from .models import User, Note
    
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret key"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    with app.app_context():
        db.create_all()
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all()
        print('Created Database!')