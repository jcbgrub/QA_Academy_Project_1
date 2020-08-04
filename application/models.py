from application import db
from datetime import datetime
# Name of the database: litary_db
# Name of testing database: literay_testing_db

# Class for the user table
class users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    main_lib = db.relationship('main_lib', backref='owner', lazy=True)

# Class for book library 
class book_lib(db.Model):
    book_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    first_name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(100), nullable=False, unique=True)
    pages = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(30), nullable=False)
    comment = db.Column(db.String(500), nullable=False)
    date_read = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    main_lib = db.relationship('main_lib', backref='bookcode', lazy=True)

# Class for the main library 
class main_lib(db.Model):
    entry_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.user_id'))
    book_id = db.Column(db.Integer,db.ForeignKey('book_lib.book_id'))
   