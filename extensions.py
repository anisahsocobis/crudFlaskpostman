from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_mail import Mail
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager
from flask_mail import Message

CORS()
db = SQLAlchemy()
ma = Marshmallow()
mail = Mail()
jwt = JWTManager()
