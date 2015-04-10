from app import auth
from flask import Blueprint
from flask_restful import Resource, Api

class Index(Resource):
	@auth.requires_auth
	def get(self):
		return {
			'status':'true',
			'message':'Welcome Oemah',
		}

blueprint = Blueprint('index', __name__)
api = Api(blueprint, prefix='/')
api.add_resource(Index, "")