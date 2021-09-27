from flask import request
from flask_restful import Resource

from src.database.models import Order, Client


class OrderWrapper(Resource):
    @classmethod
    def validate_data(cls, data):
        """
        The function used to validate data
        :param dict data: actual data to check
        :returns: None - if data is not valid, data - if success
        """

        if not data:
            return None
        if not (set(data.keys()) <= set(Order.__table__.columns.keys())):
            return None
        if 'id' not in data:
            return None
        if data['id'] is None:
            return None
        if data.get('client_name'):
            return None
        return data

    @staticmethod
    def get(client_id=None, order_id=None):
        # No arguments specified (path: path: /api/orders/)
        if not client_id and not order_id:
            return {'orders': list(map(lambda cl: cl.serialize(), Order.query.all()))}

        # Specified only Client (path: /api/orders/<int:client_id>)
        elif client_id and not order_id:
            return list(map(lambda o: o.serialize(), filter(lambda o: o.client_id == client_id, Order.query.all())))

        # Specified only Order (path: /api/order/<int:order_id>)
        elif order_id and not client_id:
            try:
                return Order.query.get(order_id).serialize()
            except AttributeError:
                return {"message": "No order found"}, 400
        # elif client_id and order_id:
        #     order = Order.query.get(order_id)
        #     if order and (order.client_id == client_id):
        #         return order.serialize(), 200
        #     else:
        #         return None, 404

    @staticmethod
    def post(self):
        data = request.get_json(force=True)
        print(data)
        # data = self.validate_data(request.get_json(force=True))
        try:
            if Order(data['client_id'], Client.query.get(data['client_id']).name, data['total']).create():
                return 200
            else:
                return None, 400
        except TypeError:
            return None, 400
        # try:
        # if self._cid and self._total:
        #     cl = Client.query().get(self._cid)
        #     if cl:
        #         order = Order(cl.id, cl.name, self._total)
        #         order.create()
        # else:
        #     return {'message': 'Wrong attributes'}, 400
        # except AttributeError:
        #     database.rollback()
        #     print("Ошибка добавления в БД")
        #     return {'message': 'Specified client does not exist'}, 400

    def patch(self):
        if request.content_type != 'application/json':
            return {'message': 'Request content type should be <application/json>'}, 400
        try:
            data = self.validate_data(request.get_json(force=True))  # CAN BE NONE
            # if data:
            order = Order.query.get(data['id'])  # CAN BE NONE
            attributes = list(data.keys())
            print(attributes)
            # if 'client_name' in attributes:
            #     raise ValueError
            for attr in attributes[1:]:
                if attr == 'client_id':
                    setattr(order, attr, data[attr])
                    setattr(order, 'client_name', Client.query.get(data['client_id']).name)

                else:
                    setattr(order, attr, data[attr])
            order.create()
        except (AttributeError, TypeError):
            return {'message': 'Specified attributes are wrong ot do not exist'}, 400

    @staticmethod
    def delete(order_id=None):
        try:
            Order.query.get(order_id).delete()
        except AttributeError:
            return {"message": "Bad request"}