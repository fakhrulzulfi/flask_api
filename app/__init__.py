from flask import Flask

from config import Config

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

from flask_bcrypt import Bcrypt

from flask_jwt_extended import JWTManager


app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


from app import routes
from app.model import models
