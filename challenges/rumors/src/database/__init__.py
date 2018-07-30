from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from challenges.rumors.src.database.models import Rumor
    db.drop_all()
    db.create_all()
