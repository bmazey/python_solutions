from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relative/challenges/rumors/src/db.sqlite'
# https://gist.github.com/ekiara/7676136 ???
db = SQLAlchemy(app)
db.create_all()
