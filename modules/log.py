# *-* coding:utf-8 *-*
import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
from beaker.middleware import SessionMiddleware
import json

'''*********Sessions Data*********'''
session_opts = {
    'session.type': 'file',
    'session.data_dir': './session',
    'session.auto': True,
    'session.timeout': 3600,
}



'''*********Läs & skriv till fil*********'''
def read_data(file):
	fileIn = open('static/data/'+ file +'.json', 'r')
	dataRead = json.load(fileIn)
	fileIn.close()				
	return dataRead


'''*********Authorisering*********'''
def validate_user(username, password):
	users = read_data('users_db')
	for user in users:
		if username.lower() == user['username'].lower() and password == user['password']:
			return True
	return False
	
def validate_autho():
	session = request.environ.get('beaker.session')
	try:
		session['userId']
		return True

	except:
		redirect('/login')
		
def is_user_logged_in():
	session = request.environ.get('beaker.session')
	try:
		session['userId']
		return True
	except:
		return False	
			
def get_user_id(username):
	users = read_data('users_db')
	for user in users:
		if username == user['username']:
			return user['id']

def get_user_id_logged_in():
	session = request.environ.get('beaker.session')
	return session['userId']

def get_user_name():
	session = request.environ.get('beaker.session')
	if get_user_level() == 1:
		users = read_data('students')
	else:
		users = read_data('employers')
	
	for user in users:
		if session['userId'] == user['id']:
			return user['first_name']

def get_user_level():
	session = request.environ.get('beaker.session')
	users = read_data('users_db')
	for user in users:
		if session['userId'] == user['id']:
			return user['autholevel']
	
		
'''*********Funktioner*********'''	
def login():
	username = request.forms.get('email')
	password = request.forms.get('password')
	if validate_user(username, password) == True:
		userID = get_user_id(username)
		session = request.environ.get('beaker.session')
		session['userId'] = userID
		session.save()
		return True
	
	else:
		return False

def log_in_new_user(email, password):
	if validate_user(email, password) == True:
		userID = get_user_id(email)
		session = request.environ.get('beaker.session')
		session['userId'] = userID
		session.save()
	


def log_out():
	session = request.environ.get('beaker.session')
	session.delete()
	session.save()

def ajax_validation():
	username = request.forms.get('email')
	password = request.forms.get('password')
	if validate_user(username, password) == True:
		return True
	
	else:
		return False
