from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
app.config['SECRET_KEY'] = getenv('SECRET_KEY')


db = SQLAlchemy(app)

from application import routes