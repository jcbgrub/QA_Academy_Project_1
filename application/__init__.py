from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv
# Imports for running the app locally
from os import environ, path
from dotenv import load_dotenv

app = Flask(__name__)

basedir = path.abspath(path.dirname(__file__))  # We find the absolute path of the root directory of our current file.
load_dotenv(path.join(basedir, '.env'))  # Load our specific .env file from the root directory of our current file.

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

db = SQLAlchemy(app)

from application import routes