from app import db

class School(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, index=True)
	location = db.Column(db.String, index=True)
	gpa = db.Column(db.Float, index=True)
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