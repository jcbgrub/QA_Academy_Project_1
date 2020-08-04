from flask import render_template, redirect, url_for
from application import app, db
from application.models import book_library, main_library
from application.forms import BookForm, RatingForm

@app.route('/')
@app.route('/main_lib', methods=['GET', 'POST'])
def main_lib():
	form = RatingForm()
	if form.validate_on_submit():
		ratingData = Rate(
			rating = form.rating.data,
			comment = form.comment.data,
			date_read = form.date_read.data
		)

		db.session.add(RatingForm)
		db.session.commit()

		return redirect(url_for('main_lib'))

	else:
		print(form.errors)

	return render_template('main_lib.html', title='My Library', form=form)

@app.route('/manage_lib', methods=['GET', 'POST'])
def manage_lib():
	form = BookForm()
	if form.validate_on_submit():
		bookData = Books(
			first_name = form.first_name.data,
			surname = form.last_name.data,
			title = form.title.data,
			pages = form.data,
			language = form.language.data
		)

		db.session.add(bookData)
		db.session.commit()

		return redirect(url_for('main_lib'))

	else:
		print(form.errors)

	return render_template('manage_lib.html', title='Manage my Entries', form=form)

@app.route('/login')
def login():
	return render_template('login.html', title='login')

@app.route('/register')
def register():
	return render_template('register.html', title='Register')