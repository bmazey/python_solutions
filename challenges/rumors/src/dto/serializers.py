from flask_restplus import fields
from challenges.rumors.src.config.restplus import api


rumor = api.model('rumor', {
    'id': fields.Integer(readOnly=True, description='unique identifier of a rumor'),
    'title': fields.String(required=True, description='rumor title'),
    'body': fields.String(required=True, description='rumor content'),
    'pub_date': fields.DateTime,
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_rumors = api.inherit('Page of blog posts', pagination, {
    'items': fields.List(fields.Nested(rumor))
})
