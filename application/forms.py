from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange
from datetime import date

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
    rating =StringField('Rate 1 to 6',validators = [NumberRange(min=1,max=6)])
    comment = StringField('Comments',validators = [Length(min=1, max=1000)])
    date_read = IntegerField('Date read', validators = [NumberRange(min=1900/1/1,max=date.today())])
    submit = SubmitField('Insert')