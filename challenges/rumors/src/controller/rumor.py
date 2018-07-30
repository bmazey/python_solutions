import logging

from flask import request
from flask_restplus import Resource
from challenges.rumors.src.service.business import create_rumor, update_rumor, delete_rumor
from challenges.rumors.src.dto.serializers import rumor, page_of_rumors
from challenges.rumors.src.config.validators import pagination_arguments
from challenges.rumors.src.config.restplus import api
from challenges.rumors.src.database.models import Rumor

log = logging.getLogger(__name__)

ns = api.namespace('rumor', description='rumor services & operations')


@ns.route('/')
class RumorCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_rumors)
    def get(self):
        """
        Returns list of blog posts.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        posts_query = Rumor.query
        posts_page = posts_query.paginate(page, per_page, error_out=False)

        return posts_page

    @api.expect(rumor)
    def post(self):
        """
        Creates a new blog post.
        """
        create_rumor(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Post not found.')
class PostItem(Resource):

    @api.marshal_with(rumor)
    def get(self, id):
        """
        Returns a blog post.
        """
        return Rumor.query.filter(Rumor.id == id).one()

    @api.expect(rumor)
    @api.response(204, 'Post successfully updated.')
    def put(self, id):
        """
        Updates a blog post.
        """
        data = request.json
        update_rumor(id, data)
        return None, 204

    @api.response(204, 'Post successfully deleted.')
    def delete(self, id):
        """
        Deletes blog post.
        """
        delete_rumor(id)
        return None, 204


@ns.route('/archive/<int:year>/')
@ns.route('/archive/<int:year>/<int:month>/')
@ns.route('/archive/<int:year>/<int:month>/<int:day>/')
class PostsArchiveCollection(Resource):

    @api.expect(pagination_arguments, validate=True)
    @api.marshal_with(page_of_rumors)
    def get(self, year, month=None, day=None):
        """
        Returns list of blog posts from a specified time period.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        start_month = month if month else 1
        end_month = month if month else 12
        start_day = day if day else 1
        end_day = day + 1 if day else 31
        start_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, start_month, start_day)
        end_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, end_month, end_day)
        posts_query = Rumor.query.filter(Rumor.pub_date >= start_date).filter(Rumor.pub_date <= end_date)

        posts_page = posts_query.paginate(page, per_page, error_out=False)

        return posts_page
