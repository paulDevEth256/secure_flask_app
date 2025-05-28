from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_bcrypt import Bcrypt
from .config import Config

db = SQLAlchemy()
jwt = JWTManager()
limiter = Limiter(key_func=get_remote_address)
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    limiter.init_app(app)
    bcrypt.init_app(app)

    from .routes import auth
    app.register_blueprint(auth)

    return app
