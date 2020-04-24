from flask import render_template, flash, url_for, redirect, request
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from planter import app, db 
from planter.models import Message, User

@app.route('/', methods = ['GET'])
def hello_world():
	return ('Hello from Fedora')


@app.route('/main', methods = ['GET'])
def main():
	return render_template('index.html', name = 'БуддаБар', title="RunAPP")


@app.route('/main2', methods = ['GET'])
@login_required
def main2():
	messages = Message.query.all()
	return render_template('page2.html', messages = messages, title = "PAGE2")


@app.route('/add_message', methods = ['POST'])
@login_required
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
@login_required
def add_motor():
	return ('Тут будем добавлять мотор')


@app.route('/register', methods = ['GET', 'POST'])
def register():
	login = request.form.get('login') 
	password = request.form.get('password')
	password2 = request.form.get('password2')

	if request.method == "POST":
		if not (login or password or password2):
			flash ('Будьте добры заполните все поля')
		elif password != password2:
			flash ('Пароли не совпадают')
		else:
			hash_pwd = generate_password_hash(password)
			new_user = User(login=login, password = hash_pwd)
			db.session.add(new_user)
			db.session.commit()

			return redirect(url_for('login_page'))


	return render_template('register_page.html')

@app.route('/login', methods = ['GET', 'POST'])
def login_page():
	login = request.form.get('login') #Т.к. с пустым полем, поймем что пользователь у нас первый раз
	password = request.form.get('password')

	if login and password:
		user = User.query.filter_by(login=login).first()

		if user and check_password_hash(user.password, password): #Пароль из базы и который получили и если совпадают то тру
			login_user(user) #Пользователь авторизован
			#Сохраним страницу откуда пришел user
			next_page = request.args.get('next')
			flash("Успешный вход")
			return redirect(next_page)

		else:
			flash("Логин или пароль введен не корректно")

	#	else:
		#flash ("Проверьте логин и пароль")

	return render_template('login_page.html')



@app.route('/logout', methods = ['GET', 'POST'])
@login_required
def logout():
	logout_user()
	return redirect(url_for('hello_world'))

@app.after_request
def redirect_to_signin(response):
	if response.status_code == 401:
		return redirect(url_for('login_page') + '?next=' + request.url )

	return response 