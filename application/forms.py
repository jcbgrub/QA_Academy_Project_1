from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, Email, EqualTo, ValidationError
from datetime import date
from application.models import Users, book_library,main_library

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
    selecttitle = SelectField("Choose the title of the book",
                        blank_text='Choose the title of the book',
                        query_factory=lambda: book_library.query.all(),
                        allow_blank=False)
    rating =StringField('Rate 1 to 6',validators = [NumberRange(min=1,max=6)])
    comment = StringField('Comments',validators = [Length(min=1, max=1000)])
    date_read = IntegerField('Date read', validators = [NumberRange(min=1900/1/1,max=date.today())])
    submit = SubmitField('Insert Review')

# updateing books
class UpdateBookForm(FlaskForm):
    first_name = StringField('First Name', validators = [DataRequired(),Length(min=1, max=30)])
    surname = StringField('Surname',validators = [DataRequired(),Length(min=1, max=30)])
    title = StringField('Title',validators = [DataRequired(),Length(min=1, max=30)])
    pages = StringField('Pages',validators = [Length(min=1, max=30)])
    language = StringField('Language',validators = [DataRequired(),Length(min=1, max=25)])
    submit = SubmitField('Update this Book')

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