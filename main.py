# *-* coding:utf-8 *-*
import bottle
from modules import log
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
from beaker.middleware import SessionMiddleware
import json

	
'''*********Routes*********'''

@route('/')
def startPage():
	return template('index')


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
	if log.validate_autho() == True: #and log.get_user_level() == 2 | kontrollerar om användaren är inloggad (returnerar true eller false)
		username = log.get_user_name() #hämtar användarens namn från DB (returnerar en sträng)
		user_level = log.get_user_level() #kollar om användaren är uppdragstagare eller student (returnerar 1 eller 2)
		if user_level == 1:
			return template('admin', user=username, level="student")
		else:
			return template('admin', user=username, level="arbetsgivare")
		
	else:
		redirect('/login') 

@error(404)
def error404(error):
    return template('pagenotfound')	
	
@route('/static/<filename:path>')
def server_static(filename):
	return static_file(filename, root="static")


app = SessionMiddleware(app(), log.session_opts)		 	 
run(app=app)		 	 