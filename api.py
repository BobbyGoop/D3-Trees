from db_setup import db_session
from db_models import *
from flask import jsonify
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('client_id', type=int, help="Enter the client id")
parser.add_argument('order_id', type=int, help="Enter the client id")


class ClientWrapper(Resource):
    def __init__(self):
        self._cid = parser.parse_args().get('client_id')

    def get(self):
        if self._cid:
            return jsonify(db_session.query(Client).get(self._cid).serialize())
        else:
            return {"clients": list(map(lambda cl: cl.serialize(), db_session.query(Client).all()))}


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
