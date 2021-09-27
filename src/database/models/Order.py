from datetime import datetime
from sqlalchemy.exc import IntegrityError
from src.database.setup import db


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
        try:
            db.session.add(self)
            db.session.commit()
            print("Added record:", self)
            return True
        except IntegrityError:
            db.session.rollback()
            print("Error")
            return False

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        print("Deleted record:", self)