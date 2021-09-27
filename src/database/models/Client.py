from sqlalchemy.exc import IntegrityError
from src.database.setup import db


class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    surname = db.Column(db.String(250))
    email = db.Column(db.String(250), unique = True)

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def __repr__(self):
        return "<{} {} {}>".format(self.id, self.name, self.surname)

    def serialize(self):
        return {"id": self.id, "name": self.name, "surname": self.surname, "email": self.email}

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