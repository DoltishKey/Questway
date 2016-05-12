# *-* coding:utf-8 *-*
import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
from beaker.middleware import SessionMiddleware
import MySQLdb
import hashlib


'''*********Sessions Data*********'''
session_opts = {
    'session.type': 'file',
    'session.data_dir': './session',
    'session.auto': True,
    'session.timeout': 3600,
}


'''*********Authorisation*********'''
def validate_user(username, password, cursor):
    '''Checks that login-information is correct'''
    password = hashlib.sha256(password).hexdigest()
    sql = "SELECT id FROM users WHERE mail = '%s' and password = '%s' " %(username, password)

    #call_database()
    cursor.execute(sql)
    mighty_db_says = cursor.fetchall()
    #hang_up_on_database()

    if len(mighty_db_says) == 1:
        user_id = mighty_db_says[0][0] #
        return {'id':user_id, 'result':True}

    else:
        return {'result':False}


def validate_autho():
    '''Checks that the user is logged in'''
    session = request.environ.get('beaker.session')
    try:
        session['userId']
        return True

    except:
        redirect('/login')

def is_user_logged_in():
    '''Checks that the user in logged in'''
    session = request.environ.get('beaker.session')
    try:
        session['userId']
        return True
    except:
        return False

def get_user_id_logged_in():
    '''Returns ID of logged in user'''
    session = request.environ.get('beaker.session')
    return session['userId']

def get_user_name(cursor):
    '''Returns First name of logged in user'''
    session = request.environ.get('beaker.session')
    if get_user_level(cursor) == 1:
        sql = "SELECT first_name FROM students WHERE id = '%d'"%(session['userId'])

    else:
        sql = "SELECT first_name FROM employers WHERE id = '%d'"%(session['userId'])

    cursor.execute(sql)
    mighty_db_says = cursor.fetchall()
    first_name = mighty_db_says[0][0]
    return first_name

def get_user_level(cursor):
    '''Returns access-level of logged in user'''
    session = request.environ.get('beaker.session')
    sql = "SELECT autho_level FROM users WHERE id = '%d'"%(session['userId'])
    cursor.execute(sql)
    mighty_db_says = cursor.fetchall()
    autho_level = mighty_db_says[0][0]
    return autho_level

'''*********Funktioner*********'''
def login(cursor):
    '''Do login'''
    username = request.forms.get('email')
    password = request.forms.get('password')
    user_status = validate_user(username, password, cursor)
    if user_status['result'] == True:
        userID = user_status['id']
        session = request.environ.get('beaker.session')
        session['userId'] = userID
        session.save()
        return True

    else:
        return False

def log_in_new_user(email, password, cursor):
    '''From creating profile - logg in'''
    user_status = validate_user(email, password, cursor)
    if user_status['result'] == True:
        userID = user_status['id']
        session = request.environ.get('beaker.session')
        session['userId'] = userID
        session.save()


def log_out():
    session = request.environ.get('beaker.session')
    session.delete()
    session.save()

def ajax_validation(cursor):
    username = request.forms.get('email')
    password = request.forms.get('password')
    user_status = validate_user(username, password, cursor)
    if user_status['result'] == True:
        return True

    else:
        return False
