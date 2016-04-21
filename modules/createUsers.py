# *-* coding:utf-8 *-*
import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
import json
from validate_email import validate_email
import MySQLdb
db = MySQLdb.connect(host="195.178.232.7", port=4040, user="AC8240", passwd="hejhej123", db="AC8240");
cursor = db.cursor()


'''*********Skriv/läsa filer*********'''
def read_data(file):
	try:
		fileIn = open('static/data/'+ file +'.json', 'r')
		dataRead = json.load(fileIn)
		fileIn.close()
	except (IOError, ValueError):
		validatekDataFile(file)
		dataRead = read_data(file)
	return dataRead

def write_to_db(users, db):
	fileOut = open('static/data/'+ db +'.json', 'w')
	json.dump(users, fileOut, indent=4)
	fileOut.close()


'''*********Validering*********'''
def validate_Username(email):
	sql = "SELECT * FROM users WHERE mail = '%s'" %(email)
	#data = call_database(sql, 'fetchall()');
	cursor.execute(sql)
	data = cursor.fetchall()
	print type(data)
	if len(data) != 0:
		return True

def validatekDataFile(file):
	'''Om databasen inte finns eller är helt tom så skapas en json-fil innehållande en tom lista.'''
	resList = []
	dataFile = open('static/data/'+ file +'.json', 'w')
	json.dump(resList, dataFile, indent=4)
	dataFile.close()

def validate_if_student_exists(userID):
	users = read_data('users_db')
	for user in users:
		if int(user['id']) == int(userID) and user['autholevel'] == 1:
			return True

'''*********funktioner*********'''
def add_new_user(email, password, user_level):
	sql = "INSERT INTO users(password, \
       autho_level, mail) \
       VALUES ('%s', '%d', '%s' )" % \
       (password, user_level, email)

	#new_user_id = call_database(sql,'lastrowid');
	cursor.execute(sql)
	new_user_id = cursor.lastrowid
	db.commit()

	return new_user_id


def add_new_employer(company_name, org_nr, first_name, last_name, new_user_id):
	org_nr = int(org_nr)
	sql = "INSERT INTO employers(first_name, \
       last_name, company_name, org_nr, id) \
       VALUES ('%s', '%s', '%s', '%d', (select id from users where id = '%d') )" %(first_name, last_name, company_name, org_nr, new_user_id)

	cursor.execute(sql)
	db.commit()

	#call_database(sql, False);

def add_new_student(first_name, last_name, program, year, new_user_id):
	program = int(program)
	year = int(year)
	sql = "INSERT INTO students(first_name, \
       last_name, education_id, education_year, id) \
       VALUES ('%s', '%s', '%d', '%d', (select id from users where id = '%d') )" %(first_name, last_name, program, year, new_user_id)

	#call_database(sql, False);
	cursor.execute(sql)
	db.commit()

def get_student_main_info(user):
	user = int(user)
	students = read_data('students')
	for student in students:
		if student['id'] == user:
			return student

def get_education_info(program, year):
	educations = read_data("education")
	for education in educations:
		if int(education["id"]) == int(program) and int(education["year"]) == int(year):
			return education
		else:
			print "Något gick fel"


'''*********Main - Funktioner*********'''
def create_employer():
	company_name = request.forms.get('company_name')
	org_nr = request.forms.get('org_nr')
	first_name = request.forms.get('first_name')
	last_name = request.forms.get('last_name')
	email = request.forms.get('email').lower()
	password = request.forms.get('password')
	user_inputs=[company_name, org_nr, first_name,last_name,email,password]
	for user_input in user_inputs:
		if user_input == None or len(user_input) == 0:
			return {'result':False, 'error': 'Inget fält får vara tomt!'}

	if validate_Username(email) == True:
		return {'result':False, 'error':'Tyvärr - en användare med samma email finns redan!'}

	elif validate_email.validate_email(email) == False:
		return {'result':False, 'error':'Du måste ange en riktig email!'}

	else:
		user_level = 2
		new_user_id = add_new_user(email, password, user_level)
		add_new_employer(company_name, org_nr, first_name, last_name, new_user_id)
		return {'result':True, 'email':email, 'password':password}


def create_student():
	first_name = request.forms.get('first_name')
	last_name = request.forms.get('last_name')
	program = request.forms.get('program')
	year = request.forms.get('year')
	email = request.forms.get('email').lower()
	password = request.forms.get('password')

	user_inputs=[first_name, last_name, program, year, email, password]
	for user_input in user_inputs:
		if user_input == None or len(user_input) == 0:
			return {'result':False, 'error': 'Inget fält får vara tomt!'}

	if validate_Username(email) == True:
		return {'result':False, 'error':'Tyvärr - en användare med samma email finns redan!'}

	elif validate_email.validate_email(email) == False:
		return {'result':False, 'error':'Du måste ange en riktig email!'}

	else:
		user_level = 1
		new_user_id = add_new_user(email, password, user_level)
		add_new_student(first_name, last_name, program, year, new_user_id)
		return {'result':True, 'email':email, 'password':password}


def ajax_new_user_validation():
	email = request.forms.get('email')
	if email == None or len(email) == 0 or validate_email.validate_email(email) == False:
		return {'result': False, 'error':'Bad input'}
	elif validate_Username(email) == True:
		return {'result': False, 'error':'User exists'}
	else:
		return {'result': True}

def show_student_profile(user):
	try:
		if validate_if_student_exists(user) == True:
			student_main_info = get_student_main_info(user)
			education_info = get_education_info(student_main_info['program'],student_main_info['year'])
			return {'exists':True, 'student_info': student_main_info, 'education_info':education_info}

		else:
			return {'exists':False}

	except ValueError:
		return {'exists':False}
