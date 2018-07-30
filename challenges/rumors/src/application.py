from flask import Flask
from flask_restplus import Resource, Api


application = Flask(__name__)
api = Api(application)


@api.route("/rumor")
class RumorRoute(Resource):
    def get(self):
        return {'brandon': 'listens to selena gomez'}


def get_app():
    return application


def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
