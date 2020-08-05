from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime
# Name of the database: litary_db
# Name of testing database: literay_testing_db

# loging manager
@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

# Class for the user table
class Users(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    main_lib = db.relationship('main_library', backref='owner', lazy=True)
    
    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])

# Class for book library 
class book_library(db.Model):
    book_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    first_name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(100), nullable=False, unique=True)
    pages = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(30), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    main_lib = db.relationship('main_library', backref='bookcode', lazy=True)

# Class for the main library 
class main_library(db.Model):
    entry_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.user_id'))
    book_id = db.Column(db.Integer,db.ForeignKey('book_library.book_id'))
    date_read = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comment = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)