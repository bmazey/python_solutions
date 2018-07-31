from flask import Flask, request
from flask_restplus import Resource, Api
from challenges.rumors.src.rumor import create_rumor
from flask_restplus import fields
# from challenges.rumors.src.dto import rumor


application = Flask(__name__)
api = Api(application)

rumor = api.model('rumor', {
    'id': fields.Integer(readOnly=True, description='unique identifier of a rumor'),
    'name': fields.String(required=True, description='rumor title'),
    'content': fields.String(required=True, description='rumor content'),
})


@api.route("/rumor")
class RumorRoute(Resource):
    def get(self):
        return {'brandon': 'listens to selena gomez'}

    @api.expect(rumor)
    @api.response(201, 'Rumor successfully created.')
    def post(self):
        create_rumor(request.json)


def get_app():
    return application


def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
