from datetime import datetime
from main import db


class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    surname = db.Column(db.String(250))
    email = db.Column(db.String(250))

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def __repr__(self):
        return "{} {} {}".format(self.id, self.name, self.surname)

    def serialize(self):
        return {"id": self.id, "name": self.name, "surname": self.surname, "email": self.email}

    def create(self):


    def delete(self):
        try:

            print(self)
            db.delete(self)
            db.commit()
        except:
            db.rollback()
            return {'message': "Such record does not exist"}, 400


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    client_name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    total = db.Column(db.Integer, nullable=False)

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

    def create(self):
        db.add(self)
        db.commit()
