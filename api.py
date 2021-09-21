from flask import jsonify, url_for, request
from flask_restful import Resource, reqparse
from werkzeug.utils import redirect

from db_models import Client, Order

parser = reqparse.RequestParser()
parser.add_argument('client_id', type=int, help="Enter the client id")
parser.add_argument('client_name', type=str, help="Enter the client name")
parser.add_argument('client_surname', type=str, help="Enter the client surname")
parser.add_argument('client_email', type=str, help="Enter the client email")

parser.add_argument('order_id', type=int, help="Enter the order id")
parser.add_argument('total', type=int, help="Enter the order id")


class ClientWrapper(Resource):
    def __init__(self):
        self._id = parser.parse_args().get('client_id')
        self._name = parser.parse_args().get('client_name')
        self._surname = parser.parse_args().get('client_surname')
        self._email = parser.parse_args().get('client_email')

    @classmethod
    def validate_data(cls, data):
        if not data:
            return None
        if not (set(data.keys()) <= set(Client.__table__.columns.keys())):
            return None
        if 'id' not in data:
            return None
        if data['id'] is None:
            return None
        return data

    def get(self):
        if self._id:
            return jsonify(Client.query().get(self._id).serialize())
        else:
            return {"clients": list(map(lambda cl: cl.serialize(), Client.query().all()))}

    def post(self):
        c = Client(self._name, self._surname, self._email)
        c.create()
            # return {'message': 'Wrong attributes'}, 400
        return redirect(url_for('register'))

    def patch(self):
        if request.content_type != 'application/json':
            return {'message': 'Request content type should be <application/json>'}, 400
        data = self.validate_data(request.get_json(force=True))
        if data:
            client = Client.query().get(data['id'])
            attributes = list(data.keys())
            for attr in attributes[1:]:
                setattr(client, attr, data[attr])
            client.create()
        else:
            return {'message': 'Specified attributes are wrong ot do not exist'}, 400

    def delete(self):
        if request.content_type != 'application/json':
            return {'message': 'Request content type should be <application/json>'}, 400
        data = self.validate_data(request.get_json(force=True))
        if data:
            if list(data.keys()) != ['id']:
                return {'message': 'The <DELETE> request must contain only one parameter: id'}, 400
            client = Client.query().get(data['id'])
            client.delete()
        else:
            return {'message': 'Wrong data passed'}, 400


class OrderWrapper(Resource):
    def __init__(self):
        self._cid = parser.parse_args().get('client_id')
        self._id = parser.parse_args().get('order_id')
        self._total = parser.parse_args().get('total')

    def get(self):
        if not self._cid and not self._id:
            return {'orders': list(map(lambda cl: cl.serialize(), Order.query.all()))}
        elif self._cid and self._id:
            ordr = Client.query().get(self._id)
            if ordr and (ordr.client_id == self._cid):
                return jsonify(ordr.serialize()), 200
            else:
                return None, 404
        elif self._cid and not self._id:
            return list(map(lambda o: o.serialize(), filter(lambda o: o.client_id == self._cid, Order.query().all())))

    def post(self):
        # try:
        if self._cid and self._total:
            cl = Client.query().get(self._cid)
            if cl:
                order = Order(cl.id, cl.name, self._total)
                order.create()
        else:
            return {'message': 'Wrong attributes'}, 400
        # except AttributeError:
        #     db.rollback()
        #     print("Ошибка добавления в БД")
        #     return {'message': 'Specified client does not exist'}, 400

    def patch(self):
        pass

    def delete(self):
        pass
