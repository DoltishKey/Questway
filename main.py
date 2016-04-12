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
	return template('login')



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
	all_adds=addmod.load_adds('ads')
	complete_adds = addmod.get_corp_name(all_adds)
	if user_level == 1:
		return template('student_start', user=username, level="student", annons=complete_adds)
	else:
		#här ska arbetsgivarnas annonser med
		userid = log.get_user_id_logged_in()
		return template('employer_start', user=username, user_id=userid,  level="arbetsgivare", annons=complete_adds)



'''********Create-user********'''
@route('/create')
def create_employer():
	return template('create_user')

@route('/create_student')
def create_student():
	return template('create_student')

@route('/create_employer')
def create_employer():
	return template('create_employer')


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
		education_info = user_profile_data['education_info']
		student_info = user_profile_data['student_info']
		return template('user_profile', user_autho = user_levle, student_id = user, student= student_info, education = education_info)

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


'''*****Ta bort annons****'''

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
			redirect('/admin')
		else:
			return 'Behörighet saknas!'

	else:
		return 'Behörighet saknas!'


'''****Studenten kan söka en annons****'''

@post('/sok_annons/<annons>')
def sok_annons(annons):
    log.validate_autho()
    all_adds=addmod.load_adds('ads')
    user=log.get_user_id_logged_in()

    what_add=addmod.choose_ad(annons, all_adds, None)

    for add in all_adds:
        if int(add['uniq_adNr'])==int(annons):
            if user in add['who_applied']:
                return "Du har redan ansökt på denna annons!"
            else:
                what_add['who_applied'].append(user)
                add['who_applied']=what_add['who_applied']

    with open('static/data/ads.json', 'w') as fil:
        json.dump(all_adds, fil, indent=4)

    redirect('/admin')


'''****Listar de studenter som sökt ett specifik uppdrag***'''

@route('/allMissions')
def list_applied_students():
    log.validate_autho()
    if log.get_user_level() == 2:
        all_adds=addmod.load_adds('ads')
        user=log.get_user_id_logged_in()
        students=log.read_data('students')
        relevant_adds=[]
        for add in all_adds:
            if user == add['creator']:
                relevant_adds.append(add)

        return template('adds.tpl', adds=relevant_adds, students=students)


'''********Övriga Routes********'''

@error(404)
def error404(error):
    return template('pagenotfound')

@route('/static/<filename:path>')
def server_static(filename):
	return static_file(filename, root="static")


app = SessionMiddleware(app(), log.session_opts)
run(app=app)
