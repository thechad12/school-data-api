from app import app, db
from models import School
from flask import render_template, jsonify, redirect, session, url_for,\
	request


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/schools/')
def schoolsSerialize():
	schools = School.query().all()
	return jsonify(schools=[s.serialize for s in schools])

