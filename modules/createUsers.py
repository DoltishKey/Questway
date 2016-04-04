# *-* coding:utf-8 *-*
import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
import json
from validate_email import validate_email



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
	users = read_data('users_db')
	for user in users:
		if user['username'].lower() == email.lower():
			return True 

def validate_org_nr(org_nr):
	organisations = read_data('employers')
	for organisation in organisations:
		if int(organisation['org_nr']) == int(org_nr):
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
	users = read_data('users_db')
	userIds = []
	for user in users:
		userIds.append(int(user['id']))
	
	if len(userIds) == 0:
		new_user_id = 1
	else:
		maximum_ID_value = max(userIds)
		new_user_id	= maximum_ID_value + 1
		
	new_user = {
		"username": email, 
        "password": password,
        "id":new_user_id,
        "autholevel":user_level
		}
	users.append(new_user)
	db = 'users_db'
	write_to_db(users, db)
	return new_user_id


def add_new_employer(company_name, org_nr, first_name, last_name, new_user_id):
	employers = read_data('employers')
	new_employer ={
		"company_name": company_name, 
        "org_nr": org_nr, 
        "first_name": first_name, 
        "last_name": last_name, 
        "id": new_user_id,
		}
	
	employers.append(new_employer)
	db = 'employers'
	write_to_db(employers, db)
	
def add_new_student(first_name, last_name, program, year, new_user_id):
	students = read_data('students')
	new_student ={
        "first_name": first_name, 
        "last_name": last_name,
        "program": program, 
        "year": year,  
        "id": new_user_id,
		}
	
	students.append(new_student)
	db = 'students'
	write_to_db(students, db)
	
def get_student_main_info(user):
	user = int(user)
	students = read_data('students')
	for student in students:
		if student['id'] == user:
			return student

def get_education_info(program, year):
	pass


'''*********Main - Funktioner*********'''		
def create_employer():
	company_name = request.forms.get('company_name')
	org_nr = request.forms.get('org_nr')
	first_name = request.forms.get('first_name')
	last_name = request.forms.get('last_name')
	email = request.forms.get('email')
	password = request.forms.get('password')
	user_inputs=[company_name, org_nr, first_name,last_name,email,password]
	for user_input in user_inputs:
		if user_input == None or len(user_input) == 0: 
			return {'result':False, 'error': 'Inget fält får vara tomt!'} 
	#org_nr = request.forms.get('org_nr')
	#if validate_Username(email) == True or validate_org_nr(org_nr) == True:
	if validate_Username(email) == True:
		return {'result':False, 'error':'Tyvärr - en användare med samma email finns redan!'}
	
	elif validate_email.validate_email(email) == False:	
		return {'result':False, 'error':'Du måste ange en riktig email!'}
		
	else:
		user_level = 2		
		new_user_id = add_new_user(email, password, user_level)
		add_new_employer(company_name, org_nr, first_name, last_name, new_user_id)
		return {'result':True}

		
def create_student():
	first_name = request.forms.get('first_name')
	last_name = request.forms.get('last_name')
	program = request.forms.get('program')
	year = request.forms.get('year')
	email = request.forms.get('email')
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
		return {'result':True}


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
			
			return {'exists':True}
			
		else:
			return {'exists':False}
	
	except ValueError:
		return {'exists':False}

	