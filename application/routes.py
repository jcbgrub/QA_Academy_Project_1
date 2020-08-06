from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt
from application.models import book_library, main_library, Users
from application.forms import BookForm, RatingForm, RegistrationForm, LoginForm, UpdateBookForm

# # Route to the login page
@app.route('/')
@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('main_lib'))
	form = LoginForm()
	if form.validate_on_submit():
		user=Users.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('main_lib'))
	return render_template('login.html', title='Login', form=form)

# Route to the main library, joining the book and ratings tables.
@app.route('/main_lib')
@login_required
def main_lib():
	BookData=book_library.query.all()
	return render_template('main_lib.html', title='main_lib')

# Route to making new book entries
@app.route('/new_entry', methods=['GET', 'POST'])
@login_required
def new_entry():
	form = BookForm()
	if form.validate_on_submit():
		bookData = book_library(
			first_name = form.first_name.data,
			surname = form.surname.data,
			title = form.title.data,
			pages = form.pages.data,
			language = form.language.data,
			b_owner=current_user
		)
		db.session.add(bookData)
		db.session.commit()
		return redirect(url_for('main_lib'))
	else:
		print(form.errors)
	return render_template('new_entry.html', title='new_entry', form=form)

# route to rating books
@app.route('/rate', methods=['GET', 'POST'])
@login_required
def rate():
	form = RatingForm()
	if form.validate_on_submit():
		ratingData = main_library(
			rating = form.rating.data,
			comment = form.comment.data,
			date_read = form.date_read.data,
			b_owner=current_user
		)
		db.session.add(RatingForm)
		db.session.commit()
		return redirect(url_for('main_lib'))
	else:
		print(form.errors)
	return render_template('rate.html', title='rate', form=form)

# Route to register a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('main_lib'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hash_pw = bcrypt.generate_password_hash(form.password.data)

		user = Users(
		first_name=form.first_name.data,
		last_name=form.last_name.data,
		email=form.email.data,
		password=hash_pw)

		db.session.add(user)
		db.session.commit()
		return redirect(url_for('new_entry'))
	return render_template('register.html', title='register', form=form)

# Route to update book entries
@app.route('/update_lib', methods=['GET', 'POST'])
@login_required
def update_lib():
	form = UpdateBookForm()
	if form.validate_on_submit():
		book_library.first_name = form.first_name.data
		book_library.surname = form.surname.data
		book_library.title = form.title.data
		book_library.pages = form.pages.data
		book_library.language = form.language.data
		db.session.commit()
		return redirect(url_for('update_lib'))
	elif request.method == 'GET':
		form.first_name = book_library.first_name.data
		form.surname = book_library.surname.data
		form.title = book_library.title.data
		form.pages = book_library.pages.data
		form.language = book_library.language.data
	return render_template('update_lib.html', title='update_lib', form=form)

# logout route
@app.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))


# delete function
# dont forget 			owner=current_user