from flask import Blueprint, render_template

auth = Blueprint('auth',__name__)

@auth.route('/')
def index():
	return render_template('welcome.html')

@auth.route("/home")
def welcome_home():
	return {'message': 'this is text'}

@auth.route("/developer_info")
def get_developer_info():
	return {
		'firstName': 'Nicholas',
		'lastName': 'Bierman'
	}