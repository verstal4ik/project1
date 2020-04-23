from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#Блок создания приложения
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from planter import models, routes

db.create_all()