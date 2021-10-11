from flask_jwt_extended import get_jwt, jwt_required
from flask_restful import Resource
from src.database.models.TokenBlocklist import TokenBlocklist


class LogoutWrapper(Resource):

	@jwt_required()
	def delete(self):
		jti = get_jwt()["jti"]

		TokenBlocklist(jti).create()
		# db.session.add(TokenBlocklist(jti=jti, created_at=now))
		# db.session.commit()
		return {'msg': "JWT revoked"}



	# def post(self):
	# 	data = request.get_json(force=True)
	# 	print(data.keys())
	# 	if list(data.keys()) != ['email', 'password']:
	# 		return None, 400
	# 	token = Client.authenticate(data['email'], data['password']).get_token()
	# 	return {'access_token': token}
