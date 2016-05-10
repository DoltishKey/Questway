# *-* coding:utf-8 *-*
#!/usr/bin/python
import bottle
from modules import log
from modules import createUsers
from modules import addmod
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
from beaker.middleware import SessionMiddleware
import MySQLdb



'''*********Routes*********'''

@route('/')
def startPage():
	if log.is_user_logged_in()==False:
		return template('login', pageTitle='Logga in')
	else:
		redirect('/admin')


'''*********Login*********'''

@route('/login')
def login():
	if log.is_user_logged_in()==False:
		return template('login', pageTitle='Logga in')
	else:
		redirect('/admin')

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
	log.validate_autho() #kontrollerar om användaren är inloggad
	username = log.get_user_name() #hämtar användarens namn från DB (returnerar en sträng)
	userid = log.get_user_id_logged_in() #hämtar användarens id
	user_level = log.get_user_level() #kollar om användaren är uppdragstagare eller student (returnerar 1 eller 2)

	if user_level == 1:
		ads_untreated=[]
		ads_ongoing=[]
		ads_finished=[]

		ads_to_apply_on=addmod.available_ads(userid)
		all_ads=addmod.sort_by_status(userid)
		for each in all_ads:
			print each
			if each[7]=='Obehandlad':
				ads_untreated.append(each)
			elif each[7]=='Vald':
				ads_ongoing.append(each)
			elif each[7]=='Avslutad':
				ads_finished.append(each)
		denied_missions = addmod.get_denied_missions(int(userid))
		return template('student_start',finished_ads=ads_finished, avail_ads=ads_to_apply_on, accepted_on=ads_ongoing, pending_ad=ads_untreated, user_id=userid, user=username, level="student", pageTitle = 'Start', denied_missions=denied_missions)

	else:
		employer_ads = addmod.get_my_ads(userid)
		students = addmod.students_that_applied(userid)
		return template('employer_start', user=username, user_id=userid,  level="arbetsgivare", annons=employer_ads, pageTitle = 'Start', students_application = students)



@route('/about_us')
def about_us_page():
    log.validate_autho() #kontrollerar om användaren är inloggad
    username = log.get_user_name() #hämtar användarens namn från DB (returnerar en sträng)
    userid = log.get_user_id_logged_in() #hämtar användarens id
    user_level = log.get_user_level() #kollar om användaren är uppdragstagare eller student (returnerar 1 eller 2)
    return template('about_us', pageTitle = 'Om Questway', user=username, user_autho=user_level, user_id=userid)

@route('/help')
def help_page():
    log.validate_autho() #kontrollerar om användaren är inloggad
    username = log.get_user_name() #hämtar användarens namn från DB (returnerar en sträng)
    userid = log.get_user_id_logged_in() #hämtar användarens id
    user_level = log.get_user_level() #kollar om användaren är uppdragstagare eller student (returnerar 1 eller 2)
    return template('help.tpl', pageTitle = 'Hjälp - Questway', user = username, user_autho=user_level, user_id = userid)

'''********Create-user********'''
@route('/create')
def create_employer():
	if log.is_user_logged_in()==False:
		return template('create_user', pageTitle='Student | Uppdragsgivare')
	else:
		redirect('/admin')

@route('/create_student')
def create_student():
	if log.is_user_logged_in()==False:
		return template('create_student', pageTitle='Skapa profil')
	else:
		redirect('/admin')

@route('/create_employer')
def create_employer():
	if log.is_user_logged_in()==False:
		return template('create_employer', pageTitle='Skapa profil')
	else:
		redirect('/admin')


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
	user = int(user)
	user_profile_data = createUsers.show_student_profile(user)
	is_user_logged_in = log.is_user_logged_in()

	grading_ads = addmod.grading_ads(user)
	grading_skills = addmod.get_ad_skills(user)
	username = ""
	this_user = False
	if is_user_logged_in == True:
		user_levle = log.get_user_level()
		username = log.get_user_name()
		logged_in_id = log.get_user_id_logged_in()
		if int(logged_in_id) == int(user):
			this_user = True
	else:
		user_levle = 0

	if user_profile_data['exists'] == True:
		education_info = user_profile_data['education_info']
		student_info = user_profile_data['student_info']
		student_name = student_info[0] + ' ' + student_info[1]
		print student_info
		return template('user_profile', user = username, user_autho = user_levle, user_id = user, student= student_info, education = education_info, pageTitle = student_name, grading = grading_ads, grading_skills = grading_skills, this_user=this_user )

	else:
		return template('error_message', pageTitle = 'Användaren finns inte!', user = username, user_autho = user_levle, user_id = user, error_message='Det har fel!')


@route('/edit_mission/<ad_id>', method="POST")
def edit_mission(ad_id):
	result = addmod.edit_mission(ad_id)
	redirect('/profiles/' + str(result))



'''********Change contact information********'''

@route('/edit')
def edit_contact_information():
	if log.get_user_level() == 2:
		username = log.get_user_name() #hämtar användarens namn från DB (returnerar en sträng)
		userid = log.get_user_id_logged_in() #hämtar användarens id
		return template('change_contact_info', pageTitle = 'Redigera kontaktuppgifter', user=username, user_id=userid)
	else:
		return "Behörighet saknas!"


'''********Ad-management********'''

@route('/do_new_ad')
def do_new_ad():
	'''Returns a view where the logged-in employer can fill in information for a new ad'''
	log.validate_autho()
	if log.get_user_level() == 2:
		username=log.get_user_name()
		return template('adsform.tpl',user=username, pageTitle = 'Annonser')
	else:
		return "Behörighet saknas!"

@route('/make_ad', method="POST")
def ad_done():
	'''Creates a new ad in the DB'''
	log.validate_autho()
	response=addmod.do_ad()
	if response['result']==True:
		redirect('/admin')
	else:
		return response['error']

@route('/make_ad')
def no_get():
	redirect('/admin')


'''*****Delete ad*****'''

@route('/del_ad/<which_ad>', method="POST")
def del_ad(which_ad):
	'''Deletes a specifik ad in the DB'''
	log.validate_autho()
	if log.get_user_level() == 2:
		user_logged_in=log.get_user_id_logged_in()
		addmod.erase_ad(which_ad, user_logged_in)
	else:
		return 'Behörighet saknas!'


'''****Students can apply on an ad****'''

@route('/apply_on_ad/<which_ad>', method="POST")
def apply_for_mission(which_ad):
	'''Onclick on template - student applies on a specifik ad'''
	log.validate_autho()
	response=addmod.applying_for_mission(which_ad)
	if response['result']==True:
		redirect('/admin')
	else:
		return response['error']


'''****All the ads and their applications listed***'''

@route('/allMissions')
def list_applied_students():
	'''lists all ads with their specific application status'''
	log.validate_autho()
	if log.get_user_level() == 2:
		user_id=log.get_user_id_logged_in()
		username=log.get_user_name()
		relevant_adds=addmod.get_my_ads(user_id)
		students_application = addmod.students_that_applied(user_id)
		feedback_info = addmod.get_given_feedback_for_employers(user_id)

		return template('adds.tpl',user_id=user_id, user=username, adds=relevant_adds, students=students_application, pageTitle='Alla uppdrag', feedback = feedback_info)
	else:
		return "Du har ej behörighet"


@route('/select_student/<ad>/<appliersID>')
def accepted_ones(ad, appliersID):
	if log.get_user_level() == 2:
		addmod.who_got_accepted(ad, appliersID)
		redirect ('/allMissions')
	else:
		return "Behörighet saknas!"


@route('/ad_done/<ad>', method="POST")
def ad_done(ad):
	log.validate_autho()
	if log.get_user_level() == 2:
		response = addmod.move_ad_to_complete(int(ad))
		if response['response'] == False:
			return response['error']
		else:
			redirect('/allMissions')
	else:
		return 'Behörighet saknas!'


@route('/give_feedback/<ad_nr>')
def give_feedback(ad_nr):
	if log.get_user_level() == 2:
		username = log.get_user_name()
		return template('feedback', adnr=ad_nr, pageTitle = 'Ge feedback', user=username )
	else:
		return "Behörighet saknas!"



'''********Övriga Routes********'''

@error(404)
def error404(error):
    return template('pagenotfound', pageTitle = 'Fel!' )

@route('/static/<filename:path>')
def server_static(filename):
	return static_file(filename, root="static")


app = SessionMiddleware(app(), log.session_opts)
run(app=app)
