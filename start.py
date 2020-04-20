from collections import namedtuple

from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:123@localhost/py_sweater'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(1024), nullable=False)

	def __init__(self, text, tags):
		self.text = text.strip()
		self.tags = [
			Tag(text=tag.strip()) for tag in tags.split(',')
		]

class Tag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(32), nullable=False)
	message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
	message = db.relationship('Message', backref=db.backref('tags'), lazy=True)


db.create_all()


@app.route('/', methods = ['GET'])
def hello_world():
	return ('Hello from Fedora')


@app.route('/main', methods = ['GET'])
def main():
	return render_template('index.html', name = 'БуддаБар', title="RunAPP")


@app.route('/main2', methods = ['GET'])
def main2():
	messages = Message.query.all()
	return render_template('page2.html', messages = messages, title = "PAGE2")


@app.route('/add_message', methods = ['POST'])
def add_message():
	text = request.form['text']
	tag = request.form['tag']
	db.session.add(Message(text, tag))
	db.session.commit()
	return redirect(url_for('main2'))


@app.route('/table')
def table():
	return render_template("table.html")

@app.route('/add_zone')
def add_zone():
	return ("add_zone")

@app.route('/add_motor')
def add_motor():
	return ('Тут будем добавлять мотор')