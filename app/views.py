from app import app, db
from models import School
from flask import render_template, jsonify, redirect, session, url_for,\
	request


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/schools/')
def schools_serialize():
	schools = School.query().all()
	return jsonify(schools=[s.serialize for s in schools])

@app.route('/schools/<int:school_id>')
def return_school(school_id):
	school_id = school_id
	school = School.query(id=school_id).one()
	return jsonify(school=school.serialize)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
	db.session.rollback()
	return render_template('500.html'), 500

@app.errorhandler(410)
def gone(error):
	return render_template('410.html'), 410

