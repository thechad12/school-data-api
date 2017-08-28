from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import sys

Base = declarative_base()

class School(Base):
	__tablename__ = 'school'

	id = Column(Integer, primary_key=True)
	name = Column(String, index=True)
	location = Column(String, index=True)
	gpa = Column(Integer, index=True)
	act = Column(Integer, index=True)
	sat = Column(Integer, index=True)
	grad_rate = Column(Integer, index=True)
	avg_salary = Column(Integer, index=True)
	grad_time = Column(Integer, index=True)
	school_size = Column(Integer, index=True)

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