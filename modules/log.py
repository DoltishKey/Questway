# *-* coding:utf-8 *-*
import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
from beaker.middleware import SessionMiddleware
import json
import MySQLdb
db = MySQLdb.connect(host="195.178.232.7", port=4040, user="AC8240", passwd="hejhej123", db="AC8240");
cursor = db.cursor()

'''*********Sessions Data*********'''
session_opts = {
    'session.type': 'file',
    'session.data_dir': './session',
    'session.auto': True,
    'session.timeout': 3600,
}



'''*********Läs & skriv till fil*********'''
def read_data(file):
	try:
		fileIn = open('static/data/'+ file +'.json', 'r')
		dataRead = json.load(fileIn)
		fileIn.close()
	except (IOError, ValueError):
		validatekDataFile(file)
		dataRead = read_data(file)
	return dataRead


'''*********Authorisering*********'''
def validate_user(username, password):
    sql = "SELECT id FROM users WHERE mail = '%s' and password = '%s' " %(username, password)
    cursor.execute(sql)
    if cursor.rowcount ==1:
        user_id = cursor.fetchall()[0][0]
        return {'id':user_id, 'result':True}

    else:
        return {'result':False}


def validatekDataFile(file):
	'''Om databasen inte finns eller är helt tom så skapas en json-fil innehållande en tom lista.'''
	resList = []
	dataFile = open('static/data/'+ file +'.json', 'w')
	json.dump(resList, dataFile, indent=4)
	dataFile.close()

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
    user_status = validate_user(username, password)
    if user_status['result'] == True:
        userID = user_status['id']
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
    user_status = validate_user(username, password)
    if user_status['result'] == True:
        return True

    else:
        return False
