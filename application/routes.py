from flask import render_template, redirect, url_for
from application import app, db
from application.models import book_library, main_library
from application.forms import BookForm, RatingForm


# Route to the login page
@app.route('/')
@app.route('/login')
def login():
	return render_template('login.html', title='login')

# Route to the main library, joining the book and ratings tables.
@app.route('/main_lib')
def main_lib():
	BookData=book_library.query.all().join(main_library)
	return render_template('main_lib.html', title='My Library')

# Route to making new book entries
@app.route('/new_entry', methods=['GET', 'POST'])
def new_entry():
	form = BookForm()
	if form.validate_on_submit():
		bookData = book_library(
			first_name = form.first_name.data,
			surname = form.surname.data,
			title = form.title.data,
			pages = form.pages.data,
			language = form.language.data
		)

		db.session.add(bookData)
		db.session.commit()

		return redirect(url_for('main_lib'))

	else:
		print(form.errors)

	return render_template('new_entry.html', title='New Entries', form=form)

# route to rating books
@app.route('/rate', methods=['GET', 'POST'])
def rate():
	form = RatingForm()
	if form.validate_on_submit():
		ratingData = main_library(
			rating = form.rating.data,
			comment = form.comment.data,
			date_read = form.date_read.data
		)

		db.session.add(RatingForm)
		db.session.commit()

		return redirect(url_for('main_lib'))

	else:
		print(form.errors)

	return render_template('rate.html', title='Rating', form=form)

# Route to register a new user
@app.route('/register')
def register():
	return render_template('register.html', title='Register')

# Route to update book entries
@app.route('/update_lib')
def update_lib():
	return render_template('update_lib.html', title='Update Entries')