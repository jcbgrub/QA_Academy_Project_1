from flask import render_template
from application import app

@app.route('/')
@app.route('/main_lib')
def main_lib():
	return render_template('main_lib.html', title='My Library')

@app.route('/login')
def login():
	return render_template('login.html', title='login')

@app.route('/manage_lib')
def manage_lib():
	return render_template('manage_lib.html', title='Manage my Entries')

@app.route('/register')
def register():
	return render_template('register.html', title='Register')