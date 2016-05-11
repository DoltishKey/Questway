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


'''*********Authorisering*********'''
def validate_user(username, password):
    password = hashlib.sha256(password).hexdigest()
    sql = "SELECT id FROM users WHERE mail = '%s' and password = '%s' " %(username, password)

    ask_it_to = ['fetchall()', 'rowcount']
    mighty_db_says = call_database(sql, ask_it_to)

    if mighty_db_says[1] == 1:
        user_id = mighty_db_says[0][0][0] #
        return {'id':user_id, 'result':True}

    else:
        return {'result':False}


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

def get_user_id_logged_in():
    session = request.environ.get('beaker.session')
    return session['userId']

def get_user_name():
    session = request.environ.get('beaker.session')
    if get_user_level() == 1:
        sql = "SELECT first_name FROM students WHERE id = '%d'"%(session['userId'])

    else:
        sql = "SELECT first_name FROM employers WHERE id = '%d'"%(session['userId'])

    ask_it_to = ['fetchall()']
    mighty_db_says = call_database(sql, ask_it_to)
    first_name = mighty_db_says[0][0][0]
    return first_name

def get_user_level():
    session = request.environ.get('beaker.session')
    sql = "SELECT autho_level FROM users WHERE id = '%d'"%(session['userId'])

    ask_it_to = ['fetchall()']
    mighty_db_says = call_database(sql, ask_it_to)
    autho_level = mighty_db_says[0][0][0]
    return autho_level

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
    user_status = validate_user(email, password)
    if user_status['result'] == True:
        userID = user_status['id']
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
