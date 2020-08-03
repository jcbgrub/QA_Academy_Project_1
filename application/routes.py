from flask import render_template
from application import app

@app.route('/')
@app.route('/main-lib')
def home():
 return render_template('main-lib.html', title='My Library')