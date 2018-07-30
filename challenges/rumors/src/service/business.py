from challenges.rumors.src.database import db
from challenges.rumors.src.database.models import Rumor


def create_rumor(data):
    title = data.get('title')
    body = data.get('body')
    rumor = Rumor(title, body)
    db.session.add(rumor)
    db.session.commit()


def update_rumor(rumor_id, data):
    rumor = Rumor.query.filter(Rumor.id == rumor_id).one()
    rumor.title = data.get('title')
    rumor.body = data.get('body')
    db.session.add(rumor)
    db.session.commit()


def delete_rumor(rumor_id):
    rumor = Rumor.query.filter(Rumor.id == rumor_id).one()
    db.session.delete(rumor)
    db.session.commit()

