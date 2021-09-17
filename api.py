from flask import jsonify, redirect, url_for, request
from flask_restful import Resource, reqparse
from db_models import *
from db_setup import db_session

parser = reqparse.RequestParser()
parser.add_argument('client_id', type=int, help="Enter the client id")
parser.add_argument('order_id', type=int, help="Enter the client id")
parser.add_argument('client_name', type=str, help="Enter the client id")
parser.add_argument('client_surname', type=str, help="Enter the client id")
parser.add_argument('client_email', type=str, help="Enter the client id")


class ClientWrapper(Resource):
    def __init__(self):
        self._id = parser.parse_args().get('client_id')
        self._name = parser.parse_args().get('client_name')
        self._surname = parser.parse_args().get('client_surname')
        self._email = parser.parse_args().get('client_email')

    @classmethod
    def validate_data(cls, data):
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

                o = Order(c.id, c.name, 0)
                db_session.add(o)
                db_session.commit()
                print("Добавлено")
            else:
                raise ValueError
        except:
            db_session.rollback()
            print("Ошибка добавления в БД")
            return {'message': 'Wrong attributes'}, 400
        return redirect(url_for('register'))

    def patch(self):
        if request.content_type != 'application/json':
            return {'message': 'Request content type should be "application/json"'}, 400
        data = self.validate_data(request.json)
        if data:
            client = db_session.query(Client).get(data['id'])
            attributes = list(data.keys())
            try:
                for attr in attributes[1:]:
                    setattr(client, attr, data[attr])
                    db_session.flush()
                db_session.commit()
            except:
                db_session.rollback()
                return {'message': 'Check the data types'}, 400
        else:
            return {'message': 'Specified attributes do not exist or could not be changed'}, 400
        print(set(data.keys()))

    def delete(self):
        pass


class OrderWrapper(Resource):
    def __init__(self):
        self._cid = parser.parse_args().get('client_id')
        self._oid = parser.parse_args().get('order_id')

    def get(self):
        if not self._cid and not self._oid:
            return {'orders': list(map(lambda cl: cl.serialize(), Order.query.all()))}
        elif self._cid and self._oid:
            ordr = db_session.query(Order).get(self._oid)
            if ordr and (ordr.client_id == self._cid):
                return jsonify(ordr.serialize()), 200
            else:
                return None, 404
        elif self._cid and not self._oid:
            return list(map(lambda o: o.serialize(), filter(lambda o: o.client_id == self._cid, db_session.query(Order).all())))

    def post(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
