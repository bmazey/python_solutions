from flask import Flask
from flask_restplus import Resource, Api
from challenges.rumors.src.rumor import Rumor, create_rumor


application = Flask(__name__)
api = Api(application)


@api.route("/rumor")
class RumorRoute(Resource):
    def get(self):
        return {'brandon': 'listens to selena gomez'}

    def post(self):
        rumor = Rumor(name='brandon', content='has a jonas brothers poster', id=1)
        create_rumor(rumor)
        return {'success': 'OK'}


def get_app():
    return application


def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
