from app import app, db
from models import School, User
from flask import render_template, jsonify, redirect, session, url_for,\
	request

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/newaccount', methods=['POST'])
def new_account():
	

# Return all schools in db
@app.route('/schools/')
def schools_serialize():
	schools = db.session.query(School).all()
	return jsonify(schools=[s.serialize for s in schools])

# Return information on specific school in db based on ID
@app.route('/schools/<int:school_id>')
def return_school(school_id):
	school_id = school_id
	school = db.session.query(School).filter_by(id=school_id).one()
	return jsonify(school=school.serialize)

# Generate auth token for new user
@app.route('/api/token')
def get_auth_token():
	token = User.gen_auth_token()
	return jsonify({'token': token.decode('ascii')})

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

