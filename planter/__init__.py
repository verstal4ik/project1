from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


#Блок создания приложения
app = Flask(__name__)
app.secret_key = "fsdfat 4935r940r fdas pfmasdl;xihjfds////sdad.$%"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app) #непосредственная иницилизация

from planter import models, routes

db.create_all()