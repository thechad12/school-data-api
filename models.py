from app import db

class School(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), index=True)
	gpa = db.Column(db.Float, index=True)
	sat = db.Column(db.Integer, index=True)
	act = db.Column(db.Integer, index=True)
	grad_rate = db.Column(db.Integer, index=True)
	location = db.Column(db.String, index=True)

	def __repr__(self):
		return '<School><id>%s</id><name>%s</name><GPA>%s</GPA><SAT>%s</		SAT><ACT>%s</ACT><GraduationRate>%s</GraduationRate><Location>\
		%s</Location></School>'


