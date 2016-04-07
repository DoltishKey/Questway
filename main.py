# *-* coding:utf-8 *-*
import bottle
from modules import log
from modules import createUsers
from modules import addmod
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
from beaker.middleware import SessionMiddleware
import json


'''*********Routes*********'''

@route('/')
def startPage():
	return template('index')



'''*********Login*********'''


@route('/login')
def login():
	return template('login')


@route('/ajax', method="POST")
def ajax_validation():
	result = log.ajax_validation()
	if result == False:
		return 'error'
	else:
		return 'ok'

@route('/do_login', method = 'POST')
def do_login():
	response = log.login()
	if response == True:
		redirect('/admin')

	else:
		return 'Tyvärr - användaren finns inte!'

@route('/log_out')
def log_out():
	log.log_out()
	redirect('/login')

@route('/admin')
def admin():
	log.validate_autho() #and log.get_user_level() == 2 | kontrollerar om användaren är inloggad
	username = log.get_user_name() #hämtar användarens namn från DB (returnerar en sträng)
	user_level = log.get_user_level() #kollar om användaren är uppdragstagare eller student (returnerar 1 eller 2)
	if user_level == 1:
		return template('admin', user=username, level="student")
	else:
		return template('admin', user=username, level="arbetsgivare")



'''********Create-user********'''

@route('/create')
def create_user():
	return template('create_user')


@route('/ajax_create_user', method="POST")
def ajax_validation():
	result = createUsers.ajax_new_user_validation()
	if result['result'] == False and result['error'] == 'Bad input':
		return 'Bad input'
	elif result['result'] == False and result['error'] == 'User exists':
		return 'User exists'
	else:
		return 'ok'


@route('/do_create_employer', method = 'POST')
def do_create_employer():
	response = createUsers.create_employer()
	if response['result'] == True:
		log.log_in_new_user(response['email'], response['password'])
		redirect('/admin')
	else:
		return response['error']

@route('/do_create_student', method = 'POST')
def do_create_employer():
	response = createUsers.create_student()
	if response['result'] == True:
		log.log_in_new_user(response['email'], response['password'])
		redirect('/admin')
	else:
		return response['error']

@route('/profiles/<user>')
def profiles(user):
	user_profile_data = createUsers.show_student_profile(user)
	is_user_logged_in = log.is_user_logged_in()
	if is_user_logged_in == True:
		user_levle = log.get_user_level()

	else:
		user_levle = 0

	if user_profile_data['exists'] == True:
		return template('user_profile', user_autho = user_levle, student_id = user)

	else:
		return 'Användaren finns inte!'



'''********Ad-management********'''

@route('/showadds')
def show_adds():
    log.validate_autho()
    all_adds=addmod.load_adds('ads')
    complete_adds = addmod.get_corp_name(all_adds)
    return template('adsform.tpl', annons=complete_adds)

@post('/make_ad')
def ad_done():
    log.validate_autho()
    if log.get_user_level() == 2:
    	addmod.do_ad()

    else:
    	return 'Behörighet saknas!'


@post('/del_ad/<annons>')
def del_ad(annons):
	log.validate_autho()
	if log.get_user_level() == 2:
		all_adds=addmod.load_adds('ads')
		which_ad_to_delete=addmod.choose_ad(annons, all_adds, 'Ingen vald')
		if which_ad_to_delete['creator'] == log.get_user_id_logged_in():
			all_adds.remove(which_ad_to_delete)
			with open('static//data/ads.json', 'w') as fil:
				json.dump(all_adds, fil, indent=4)
			redirect('/showadds')
		else:
			return 'Behörighet saknas!'

	else:
		return 'Behörighet saknas!'


'''********Övriga Routes********'''

@error(404)
def error404(error):
    return template('pagenotfound')

@route('/static/<filename:path>')
def server_static(filename):
	return static_file(filename, root="static")


app = SessionMiddleware(app(), log.session_opts)
run(app=app)
