from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/db.sqlite'
db = SQLAlchemy(app)


class Rumor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Rumor %r>' % self.content


db.create_all()
db.session.commit()


def create_rumor(rumor):
    db.session.add(rumor)
    db.session.commit()
