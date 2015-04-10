from app import auth
from flask import Blueprint
from flask_restful import reqparse, abort, Api, Resource

USERS = {
	'user1': {'name':'mike', 'email':'oemah@gmail.com'},
	'user2': {'name':'ali', 'email':'oemah@gmail.com'},
	'user3': {'name':'sanjay', 'email':'oemah@gmail.com'},
}

def abort_if_user_not_exist(idUser):
	if idUser not in USERS:
		abort(404, message="User {} does not exist".format(idUser))

parser = reqparse.RequestParser()
parser.add_argument('user', type=int)

class User(Resource):
	@auth.requires_auth
	def get(self, idUser):
		abort_if_user_not_exist(idUser)
		return USERS[idUser]

	def delete(self, idUser):
		abort_if_user_not_exist(idUser)
		del USERS[idUser]
		return '', 204

	def put(self, idUser):
		args = parser.parse_args()
		name = {'name':args['name'], 'email':args['email']}
		USERS[idUser] = name
		return user, 201

class UserList(Resource):
	@auth.requires_auth
	def get(self):
		return USERS

	def post(self):
		args = parser.parse_args()
		idUser = 'user%d' % (len(USERS)+1)
		USERS[idUser] = {'name':args['name'], 'email':args['email']}
		return USERS[idUser], 201

user = Blueprint('user', __name__)
api = Api(user, prefix='/')
api.add_resource(User, 'user/<string:idUser>')
api.add_resource(UserList, 'userlist')