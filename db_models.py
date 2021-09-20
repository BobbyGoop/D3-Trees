from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from db_setup import Base


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    surname = Column(String(250))
    email = Column(String(250), unique=True)

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def __repr__(self):
        return "{} {} {}".format(self.id, self.name, self.surname)

    def serialize(self):
        return {"id": self.id, "name": self.name, "surname": self.surname, "email": self.email}


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    client_name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    total = Column(Integer, nullable=False)

    def __init__(self, client_id, client_name, total):
        self.client_id = client_id
        self.client_name = client_name
        self.total = total
        self.created_at = datetime.now()

    def __repr__(self):
        return "{} {} {}".format(self.id, self.client_name, self.total)

    def serialize(self):
        return {"id": self.id, "client_name": self.client_name,
                "client_id": self.client_id, "created_at": str(self.created_at),
                "total": self.total}
