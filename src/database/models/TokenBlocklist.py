from datetime import datetime, timezone, timedelta
from src.database.setup import db
from sqlalchemy.exc import IntegrityError


class TokenBlocklist(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	jti = db.Column(db.String(36), nullable=False)
	created_at = db.Column(db.DateTime, nullable=False)

	def __init__(self, jti):
		self.jti = jti
		self.created_at = datetime.now(timezone.utc)

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
