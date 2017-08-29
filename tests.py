import os
import unittest
from config import basedir
from app import app, db
import config
from app.models import School

class TestCase(unittest.TestCase):
	def set(self):
		app.config['TEST'] = True
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'edu.db')
		db.create_all()

	def remove(self):
		db.session.remove()
		db.drop_all()

	def testSchool(self):
		school = School(name="Duquesne University",
			location="Pittsburgh, Pennsylvania", gpa=3.24, act=24,
			sat=1350, grad_rate=78, avg_salary=50000, grad_time=4,
			school_size=10000)
		db.session.add(school)
		db.session.commit()

if __name__ == '__main__':
	unittest.main()