# *-* coding:utf-8 *-*
import bottle
from bottle import route, get, post, run, template, error, static_file, request, abort, response, app
from validate_email import validate_email
import MySQLdb
import hashlib


'''*********Validation*********'''
def validate_Username(email, cursor):
    '''check that the email do not already exist in DB'''
    sql = "SELECT * FROM users WHERE mail = '%s'" %(email)
    cursor.execute(sql)
    mighty_db_says = cursor.fetchall()

    if mighty_db_says:
        return True

def validate_if_student_exists(userID, cursor):
    '''Check that there is a student with a specific user-id'''
    sql = "SELECT autho_level FROM users WHERE id = '%d'"%(userID)
    cursor.execute(sql)
    mighty_db_says = cursor.fetchall()
    if len(mighty_db_says) != 0:
        if mighty_db_says[0][0] == 1:
            return True

'''*********Funktions*********'''
def add_new_user(email, password, user_level, cursor):
    '''Creates a new user based on userinput'''
    password = hashlib.sha256(password).hexdigest()
    sql = "INSERT INTO users(password, \
       autho_level, mail) \
       VALUES ('%s', '%d', '%s' )" % \
       (password, user_level, email)

    cursor.execute(sql)
    mighty_db_says =cursor.lastrowid
    return mighty_db_says


def add_new_employer(company_name, org_nr, first_name, last_name, new_user_id, cursor):
    '''Instance of User - Creates an employer in the DB'''
    org_nr = int(org_nr)
    sql = "INSERT INTO employers(first_name, \
       last_name, company_name, org_nr, id) \
       VALUES ('%s', '%s', '%s', '%d', (select id from users where id = '%d') )" \
       %(first_name, last_name, company_name, org_nr, new_user_id)
    cursor.execute(sql)


def add_new_student(first_name, last_name, program, year, new_user_id, phone_nr, cursor):
    ''' Instance of User - Creates a student in the DB'''
    program = int(program)
    year = int(year)
    phone_nr= int(phone_nr)
    sql = "INSERT INTO students(first_name, last_name, phone, education_id, education_year, id) \
       VALUES ('%s', '%s', '%d' , (select education_id from education where education_id = '%d' and year = '%d'), \
       (select year from education where year = '%d' and education_id = '%d'), (select id from users where id = '%d'))" %(first_name, last_name, phone_nr, program, year, year, program, new_user_id)
    cursor.execute(sql)


def get_student_main_info(user, cursor):
    '''Retrieve generall information about a student in the DB'''
    sql = "SELECT students.*, users.mail FROM users JOIN students on users.id = students.id WHERE students.id = '%d'"%(user)
    cursor.execute(sql)
    mighty_db_says = cursor.fetchall()
    user_info = mighty_db_says[0]
    return user_info

def get_education_info(program, year, cursor):
    '''Retrieve all information about a program based on year/which program'''
    sql = "SELECT titel, tagline, main_info_one, main_info_two, main_info_three, img_url \
    FROM education WHERE education_id = '%d' AND year = '%d'"%(program, year)
    cursor.execute(sql)
    mighty_db_says=cursor.fetchall()
    education_info = mighty_db_says[0]

    sql = sql = "SELECT skill FROM education_skills\
    WHERE education_id = '%d' AND education_year = '%d'"%(program, year)
    cursor.execute(sql)
    education_skills = cursor.fetchall()
    return {'education_info':education_info, 'education_skills':education_skills}


'''*********Main - Functions*********'''
def create_employer(cursor):
    '''Prepair the information before creating an employer-profile'''
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

    if validate_Username(email, cursor) == True:
        return {'result':False, 'error':'Tyvärr - en användare med samma email finns redan!'}

    elif validate_email.validate_email(email) == False:
        return {'result':False, 'error':'Du måste ange en riktig email!'}

    else:
        user_level = 2
        new_user_id = add_new_user(email, password, user_level, cursor)
        add_new_employer(company_name, org_nr, first_name, last_name, new_user_id, cursor)
        return {'result':True, 'email':email, 'password':password}


def create_student(cursor):
    '''Prepair the information before creating a student-profile'''
    first_name = request.forms.get('first_name')
    last_name = request.forms.get('last_name')
    program = request.forms.get('program')
    year = request.forms.get('year')
    email = request.forms.get('email').lower()
    phone = request.forms.get('phone')
    password = request.forms.get('password')

    user_inputs=[first_name, last_name, program, year, email,phone, password]
    for user_input in user_inputs:
        if user_input == None or len(user_input) == 0:
            return {'result':False, 'error': 'Inget fält får vara tomt!'}

    if validate_Username(email, cursor) == True:
        return {'result':False, 'error':'Tyvärr - en användare med samma email finns redan!'}

    elif validate_email.validate_email(email) == False:
        return {'result':False, 'error':'Du måste ange en riktig email!'}

    else:
        user_level = 1
        new_user_id = add_new_user(email, password, user_level, cursor)
        add_new_student(first_name, last_name, program, year, new_user_id, phone, cursor)
        return {'result':True, 'email':email, 'password':password}


def ajax_new_user_validation(cursor):
	email = request.forms.get('email')
	if email == None or len(email) == 0 or validate_email.validate_email(email) == False:
		return {'result': False, 'error':'Bad input'}
	elif validate_Username(email, cursor) == True:
		return {'result': False, 'error':'User exists'}
	else:
		return {'result': True}

def show_student_profile(user,cursor):
    '''Retrieves all information for a students profile-page'''
    try:
        if validate_if_student_exists(user,cursor) == True:
            student_main_info = get_student_main_info(user, cursor)
            education_info = get_education_info(student_main_info[2],student_main_info[3], cursor)
            return {'exists':True, 'student_info': student_main_info, 'education_info':education_info}

        else:
            return {'exists':False}

    except ValueError:
        return {'exists':False}
