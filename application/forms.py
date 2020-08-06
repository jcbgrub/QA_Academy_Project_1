from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField, SelectField, DateField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Email, EqualTo
from wtforms_components import DateRange
from datetime import date, datetime
from application.models import Users, book_library, main_library

# Insert a new book into the library form
class BookForm(FlaskForm):
    first_name = StringField('First Name', validators = [DataRequired(),Length(min=1, max=30)])
    surname = StringField('Surname',validators = [DataRequired(),Length(min=1, max=30)])
    title = StringField('Title',validators = [DataRequired(),Length(min=1, max=30)])
    pages = StringField('Pages',validators = [Length(min=1, max=30)])
    language = StringField('Language',validators = [DataRequired(),Length(min=1, max=25)])
    submit = SubmitField('Insert')

# Insert a new rating into the library 
class RatingForm(FlaskForm):
    select_title = SelectField("Choose the title of the book",choices=[])
    rating =IntegerField('Rate 1 to 6',validators = [NumberRange(min=1,max=6)])
    comment = StringField('Comments',validators = [Length(min=1, max=1000)])
    date_read = DateField('Date read format:yyyy-m-d', validators = [DateRange(min=datetime(1999, 1, 1),max=datetime(3000, 1, 1))])
    submit = SubmitField('Insert Review')

# updateing books
class UpdateBookForm(FlaskForm):
    first_name = StringField('First Name', validators = [DataRequired(),Length(min=1, max=30)])
    surname = StringField('Surname',validators = [DataRequired(),Length(min=1, max=30)])
    title = StringField('Title',validators = [DataRequired(),Length(min=1, max=30)])
    pages = StringField('Pages',validators = [Length(min=1, max=30)])
    language = StringField('Language',validators = [DataRequired(),Length(min=1, max=25)])
    submit = SubmitField('Update this Book')

# this is the registartion form.
class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',validators=[DataRequired(),Length(min=2, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(),Length(min=3, max=30)])
    email = StringField('Email', validators = [DataRequired(),Email()])
    password = PasswordField('Password',validators = [DataRequired(),])
    confirm_password = PasswordField('Confirm Password',validators = [DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already registered')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')