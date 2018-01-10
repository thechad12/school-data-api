from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, )
import sys
from app import db


class School(db.Model):
	__tablename__ = 'school'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, index=True)
	location = db.Column(db.String, index=True)
	gpa = db.Column(db.Integer, index=True)
	act = db.Column(db.Integer, index=True)
	sat = db.Column(db.Integer, index=True)
	grad_rate = db.Column(db.Integer, index=True)
	avg_salary = db.Column(db.Integer, index=True)
	grad_time = db.Column(db.Integer, index=True)
	school_size = db.Column(db.Integer, index=True)

	@property
	def serialize(self):
		return {
			'id': self.id,
			'name': self.name,
			'location': self.location,
			'gpa': self.gpa,
			'act': self.act,
			'sat': self.sat,
			'graduation_rate': self.grad_rate,
			'average_starting_salary': self.avg_salary,
			'average_graduation_time': self.grad_time,
			'school_size': self.school_size
		}

class User(db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String)
	auth_token = db.Column(db.String)

	def gen_auth_token(self):
		s = Serializer(app.config['SECRET_KEY'])
		return s.dumps({'id': self.id})

	@staticmethod
	def verify_token(token):
		s = Serializer(app.config['SECRET_KEY'])
		try:
			data = s.loads(token)
		except BadSignature:
			return None
		user = User.query.get(data['id'])
		return user

