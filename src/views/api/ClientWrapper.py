from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from src.database.models.Client import Client


class ClientWrapper(Resource):

    @classmethod
    def validate_data(cls, data):
        """
          The function used to validate data
          :param dict data: actual data to check
          :returns: None - if data is not valid, data - if success
          """

        if not data:
            return None
        if not (set(data.keys()) <= set(Client.__table__.columns.keys())):
            return None
        if 'id' not in data:
            return None
        if data['id'] is None:
            return None
        return data

    @staticmethod
    @jwt_required()
    def get(client_id=None):
        data = request.data
        print(data)
        Client.query.get(client_id)
        try:
            return Client.query.get(client_id).serialize() if client_id else \
                list(map(lambda cl: cl.serialize(), Client.query.all()))
        except AttributeError:
            return {"message": "Bad request"}

    @staticmethod
    def post():
        data = request.get_json(force=True)
        print(data)
        return 200
        # data = self.validate_data(request.get_json(force=True))
        # try:
        #     client = Client(data['name'], data['surname'], data['email'], data['password'])
        #     client.create()
        #     return {"access_token": client.get_token()}
        # except (TypeError, KeyError):
        #     return {"message": "Bad request"}, 400

    def patch(self):
        if request.content_type != 'application/json':
            return {'message': 'Request content type should be <application/json>'}, 400
        data = self.validate_data(request.get_json(force=True))
        if data:
            client = Client.query.get(data['id'])
            attributes = list(data.keys())
            for attr in attributes[1:]:
                setattr(client, attr, data[attr])
            client.create()
        else:
            return {'message': 'Specified attributes are wrong ot do not exist'}, 400

    @staticmethod
    def delete(client_id=None):
        # data = request.data
        # print(data)
        try:
            Client.query.get(client_id).delete()
        except AttributeError:
            return {"message": "Bad request"}
