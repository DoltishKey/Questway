# *-* coding:utf-8 *-*
import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
from validate_email import validate_email
import MySQLdb
import hashlib

'''*********DB info*********'''
def call_database(sql, asked_from_cursor):
    db = MySQLdb.connect(host="195.178.232.16", port=3306, user="AC8240", passwd="hejhej123", db="AC8240");
    cursor = db.cursor()
    cursor_answer = []
    try:
        cursor.execute(sql)
        for query in asked_from_cursor:
            cursor_answer.append(eval('cursor.'+query))
        db.commit()

    except:
        db.rollback()

    db.close()
    return cursor_answer


'''*********Validering*********'''
def validate_Username(email):
	sql = "SELECT * FROM users WHERE mail = '%s'" %(email)
	ask_it_to = ['rowcount']
	mighty_db_says = call_database(sql, ask_it_to)

	if mighty_db_says[0] != 0:
		return True

def validate_if_student_exists(userID):
	sql = "SELECT autho_level FROM users WHERE id = '%d'"%(userID)
	ask_it_to = ['fetchall()']
	mighty_db_says = call_database(sql, ask_it_to)
	if mighty_db_says[0][0][0] == 1:
		return True

'''*********funktioner*********'''
def add_new_user(email, password, user_level):
    password = hashlib.sha256(password).hexdigest()
    sql = "INSERT INTO users(password, \
       autho_level, mail) \
       VALUES ('%s', '%d', '%s' )" % \
       (password, user_level, email)

    ask_it_to = ['lastrowid']
    mighty_db_says = call_database(sql, ask_it_to)
    new_user_id = mighty_db_says[0]

    return new_user_id


def add_new_employer(company_name, org_nr, first_name, last_name, new_user_id):
	org_nr = int(org_nr)
	sql = "INSERT INTO employers(first_name, \
       last_name, company_name, org_nr, id) \
       VALUES ('%s', '%s', '%s', '%d', (select id from users where id = '%d') )" \
	   %(first_name, last_name, company_name, org_nr, new_user_id)

	ask_it_to = []
	mighty_db_says = call_database(sql, ask_it_to)


def add_new_student(first_name, last_name, program, year, new_user_id):
	program = int(program)
	year = int(year)
	sql = "INSERT INTO students(first_name, last_name, education_id, education_year, id) \
       VALUES ('%s', '%s', (select education_id from education where education_id = '%d' and year = '%d'), \
	    (select year from education where year = '%d' and education_id = '%d'), (select id from users where id = '%d') )" \
		%(first_name, last_name, program, year, year, program, new_user_id)

	ask_it_to = []
	mighty_db_says = call_database(sql, ask_it_to)

def get_student_main_info(user):
	sql = "SELECT * FROM students WHERE id = '%d'"%(user)
	ask_it_to = ['fetchall()']
	mighty_db_says = call_database(sql, ask_it_to)
	user_info = mighty_db_says[0][0]
	return user_info

def get_education_info(program, year):
	sql = "SELECT titel, tagline, main_info_one, main_info_two, main_info_three, img_url \
	FROM education WHERE education_id = '%d' AND year = '%d'"%(program, year)
	ask_it_to = ['fetchall()']
	mighty_db_says = call_database(sql, ask_it_to)
	education_info = mighty_db_says[0][0]

	sql = sql = "SELECT skill FROM education_skills\
	WHERE education_id = '%d' AND education_year = '%d'"%(program, year)
	ask_it_to = ['fetchall()']
	mighty_db_says = call_database(sql, ask_it_to)
	education_skills = mighty_db_says[0]
	return {'education_info':education_info, 'education_skills':education_skills}


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
			education_info = get_education_info(student_main_info[2],student_main_info[3])
			return {'exists':True, 'student_info': student_main_info, 'education_info':education_info}

		else:
			return {'exists':False}

	except ValueError:
		return {'exists':False}
