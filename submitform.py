from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import Form 
from wtforms import StringField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

class SubmittForm(Form):
	name = StringField('name', validators=[InputRequired()])

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = SubmittForm(request.form)
	if request.method == 'POST':
		name=request.form['name']
		return 'welcome %s' %name
	return render_template('Submit.html', form = form)
	

@app.route("/welcome/<string:name>")
def welcome(name):
	return "Welcome " + name

if __name__ == '__main__':
	app.debug=True
	app.run('127.0.0.1')