from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'a2abc6e76d6ba36a2badac102b564db68272f444a1b20a2f'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db.init_app(app)

    from app.routes import auth
    app.register_blueprint(auth)

    return app
