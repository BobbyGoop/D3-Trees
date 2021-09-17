from flask import jsonify, redirect, url_for, request
from flask_restful import Resource, reqparse
from db_models import *
from db_setup import db_session

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
            return jsonify(db_session.query(Client).get(self._id).serialize())
        else:
            return {"clients": list(map(lambda cl: cl.serialize(), db_session.query(Client).all()))}

    def post(self):
        try:
            if self._name and self._surname and self._email:
                c = Client(self._name, self._surname, self._email)
                db_session.add(c)
                db_session.flush()

                db_session.add(Order(c.id, c.name, 0))
                db_session.commit()
                print("Добавлено")
            else:
                raise ValueError
        except AttributeError:
            db_session.rollback()
            print("Ошибка добавления в БД")
            return {'message': 'Wrong attributes'}, 400
        return redirect(url_for('register'))

    def patch(self):
        if request.content_type != 'application/json':
            return {'message': 'Request content type should be <application/json>'}, 400
        data = self.validate_data(request.get_json(force=True))
        if data:
            client = db_session.query(Client).get(data['id'])
            attributes = list(data.keys())
            try:
                for attr in attributes[1:]:
                    setattr(client, attr, data[attr])
                    db_session.flush()
                db_session.commit()
            except AttributeError:
                db_session.rollback()
                return {'message': 'Check the data types'}, 400
        else:
            return {'message': 'Specified attributes are wrong ot do not exist'}, 400

    def delete(self):
        if request.content_type != 'application/json':
            return {'message': 'Request content type should be <application/json>'}, 400
        data = self.validate_data(request.get_json(force=True))
        if data:
            if list(data.keys()) != ['id']:
                return {'message': 'The <DELETE> request must contain only one parameter: id'}, 400
            try:
                client = db_session.query(Client).get(data['id'])
                print(client)
                db_session.delete(client)
                db_session.commit()
            except:
                db_session.rollback()
                return {'message': "Such record does not exist"}, 400
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
            ordr = db_session.query(Order).get(self._id)
            if ordr and (ordr.client_id == self._cid):
                return jsonify(ordr.serialize()), 200
            else:
                return None, 404
        elif self._cid and not self._id:
            return list(map(lambda o: o.serialize(), filter(lambda o: o.client_id == self._cid, db_session.query(Order).all())))

    def post(self):
        try:
            if self._cid and self._total:
                c = db_session.query(Client).get(self._cid)
                db_session.add(Order(c.id, c.name, self._total))
                db_session.commit()
                print("Добавлено")
            else:
                return {'message': 'Wrong attributes'}, 400
        except AttributeError:
            db_session.rollback()
            print("Ошибка добавления в БД")
            return {'message': 'Specified client does not exist'}, 400

    def patch(self):
        pass

    def delete(self):
        pass
