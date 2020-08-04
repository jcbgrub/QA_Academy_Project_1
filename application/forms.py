from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from datetime import date

# Insert a new book into the library form
class BookForm(FlaskForm):
    first_name = StringField('First Name', validators = [DataRequired(),Length(min=2, max=30)])
    surname = StringField('Surname',validators = [DataRequired(),Length(min=2, max=30)])
    title = StringField('Title',validators = [DataRequired(),Length(min=2, max=30)])
    pages = StringField('Pages',validators = [Length(min=2, max=30)])
    language = StringField('Language',validators = [DataRequired(),Length(min=2, max=25)])
    comment = StringField('Comments',validators = [Length(min=2, max=1000)])
    release_year = IntegerField('Release Year : ', validators = [NumberRange(min=1900,max=date.today().year)])
    submit = SubmitField('Insert')