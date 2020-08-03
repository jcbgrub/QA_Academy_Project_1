from flask import render_template
from application import app

@app.route('/')
@app.route('/main-lib')
def home():
	return render_template('main-lib.html', title='My Library')

@app.route('/login')
def home():
	return render_template('login.html', title='login')

@app.route('/manage-lib')
def home():
	return render_template('manage-lib', title='Manage my Entries')

@app.route('/register')
def home():
	return render_template('register.html', title='Register')