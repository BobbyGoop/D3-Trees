from sqlalchemy.exc import IntegrityError
from src.database.setup import db
from flask_jwt_extended import create_access_token
from datetime import timedelta
from passlib.hash import bcrypt


class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    surname = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = bcrypt.hash(password)

    def __repr__(self):
        return "<{} {} {}>".format(self.id, self.name, self.surname)

    def serialize(self):
        return {"id": self.id, "name": self.name, "surname": self.surname, "email": self.email}

    def get_token(self, expire_time=10):
        return create_access_token(
            identity=self.id,
            expires_delta=timedelta(seconds=expire_time))

    @classmethod
    def authenticate(cls, email, password):
        user = cls.query.filter(cls.email == email).one()
        if not bcrypt.verify(password, user.password):
            return None
        return user

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