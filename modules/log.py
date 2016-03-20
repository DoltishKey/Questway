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
		if username == user['name'] and password == user['password']:
			return True
	return False
	
def validate_autho():
	session = request.environ.get('beaker.session')
	try:
		session['userId']
		return True

	except:
		redirect('/login')
			
def get_user_id(username):
	users = read_data('users_db')
	for user in users:
		if username == user['name']:
			return user['id']

def get_user_name():
	session = request.environ.get('beaker.session')
	users = read_data('users_db')
	for user in users:
		if session['userId'] == user['id']:
			return user['name']

def get_user_level():
	session = request.environ.get('beaker.session')
	users = read_data('users_db')
	for user in users:
		if session['userId'] == user['id']:
			return user['autholevel']
	
		
'''*********Funktioner*********'''	
def login():
	username = request.forms.get('username')
	password = request.forms.get('password')
	if validate_user(username, password) == True:
		userID = get_user_id(username)
		session = request.environ.get('beaker.session')
		session['userId'] = userID
		session.save()
		return True
	
	else:
		return False

def log_out():
	session = request.environ.get('beaker.session')
	session.delete()
	session.save()

def ajax_validation():
	username = request.forms.get('username')
	password = request.forms.get('password')
	print username
	print password
	if validate_user(username, password) == True:
		return True
	
	else:
		return False
