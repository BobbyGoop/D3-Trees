from flask import request
from flask_restful import Resource

from src.database.models.Client import Client


class LoginWrapper(Resource):

	def post(self):
		data = request.get_json(force=True)
		print(data.keys())
		if list(data.keys()) != ['email', 'password']:
			return None, 400
		token = Client.authenticate(data['email'], data['password']).get_token()
		return {'access_token': token}
