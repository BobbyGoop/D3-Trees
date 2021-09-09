from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from db_setup import Base


class Client(Base):
	__tablename__ = 'clients'
	id = Column(Integer, primary_key=True)
	name = Column(String(250))
	surname = Column(String(250))
	email = Column(String(250))

	def __init__(self, name, surname, email):
		self.name = name
		self.surname = surname
		self.email = email

	def __repr__(self):
		return '<User %r>' % self.name


class Order(Base):
	__tablename__ = 'orders'
	id = Column(Integer, primary_key=True)
	client_id = Column(Integer, ForeignKey('clients.id'))
	client_name = Column(String, nullable=False)
	total = Column(Integer, nullable=False)

	def __init__(self, client_id, client_name, total):
		self.client_id = client_id
		self.client_name = client_name
		self.total = total

	def __repr__(self):
		return '<Order %r: date %r, client: %r>' % (self.id, self.date, self.client_id)
