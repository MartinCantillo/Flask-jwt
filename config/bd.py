from flask import Flask
from flask_jwt_extended import JWTManager
from  flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost/ejemplo_jwt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key="secret123"
bd =SQLAlchemy(app)
ma=Marshmallow(app)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret-jwt"
jwt = JWTManager(app)