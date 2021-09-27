from .ClientWrapper import ClientWrapper
from .OrderWrapper import OrderWrapper


def initialise_resources(api):
	api.add_resource(ClientWrapper, '/api/clients/', '/api/clients/<int:client_id>')
	api.add_resource(OrderWrapper, '/api/orders/', '/api/orders/<int:client_id>', '/api/order/<int:order_id>')
