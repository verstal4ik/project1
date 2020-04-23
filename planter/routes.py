from flask import render_template, url_for, redirect, request

from planter import app, db 
from planter.models import Message

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