# *-* coding:utf-8 *-*
#!/usr/bin/python
import bottle
from modules import log
from modules import createUsers
from modules import addmod
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
from beaker.middleware import SessionMiddleware
import json
import MySQLdb



'''*********Routes*********'''

@route('/')
def startPage():
	return template('login', pageTitle='Logga in')


'''*********Login*********'''


@route('/login')
def login():
	return template('login', pageTitle='Logga in')

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
		ads_to_apply_on=[]
		not_applied_on = addmod.available_ads(userid)
		for each in not_applied_on:
			if each[7]!='Obehandlad' and each[6]==userid or each[7]==None:
				print "hej"
				ads_to_apply_on.append(each)
		ads_untreated = addmod.sort_by_status(userid,'Obehandlad')
		ads_ongoing = addmod.sort_by_status(userid,'vald')
		ads_finished = addmod.sort_by_status(userid,'Avslutad')
		denied_missions = addmod.get_denied_missions(userid)

		return template('student_start',finished_ads=ads_finished, avail_ads=ads_to_apply_on, accepted_on=ads_ongoing, pending_ad=ads_untreated, user_id=userid, user=username, level="student", pageTitle = 'Start', denied_missions = denied_missions)
	else:
		employer_ads = addmod.get_my_ads(userid)
		students = addmod.students_that_applied(userid)
		return template('employer_start', user=username, user_id=userid,  level="arbetsgivare", annons=employer_ads, pageTitle = 'Start', students_application = students)

'''
edited out from line 72 in RETURN template(student_start):

gradings = grading_ads,

'''


'''********Create-user********'''
@route('/create')
def create_employer():
	return template('create_user', pageTitle='Student | Uppdragsgivare')

@route('/create_student')
def create_student():
	return template('create_student', pageTitle='Skapa profil')

@route('/create_employer')
def create_employer():
	return template('create_employer', pageTitle='Skapa profil')


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
	#grading_ads = sorted( (addmod.read_data('grading')), key=lambda x: x['display'])
	grading_ads = addmod.grading_ads(user)
	username = ""
	if is_user_logged_in == True:
		user_levle = log.get_user_level()
		username = log.get_user_name()
	else:
		user_levle = 0

	if user_profile_data['exists'] == True:
		education_info = user_profile_data['education_info']
		student_info = user_profile_data['student_info']
		student_name = student_info[0] + ' ' + student_info[1]
		return template('user_profile', user = username, user_autho = user_levle, user_id = user, student= student_info, education = education_info, pageTitle = student_name, grading = grading_ads )

	else:
		return 'Användaren finns inte!'


@route('/ajax_edit_mission/<ad_id>', method="POST")
def ajax_edit_mission(ad_id):
	result = addmod.ajax_edit_mission(ad_id)
	redirect('/profiles/39')



'''********Change contact information********'''

@route('/edit')
def edit_contact_information():
    username = log.get_user_name() #hämtar användarens namn från DB (returnerar en sträng)
    userid = log.get_user_id_logged_in() #hämtar användarens id
    return template('change_contact_info', pageTitle = 'Redigera kontaktuppgifter', user=username, user_id=userid)


'''********Ad-management********'''

@route('/showadds')
def show_adds():
	log.validate_autho()
	username=log.get_user_name()


	return template('adsform.tpl',user=username, pageTitle = 'Annonser' )

@post('/make_ad')
def ad_done():
	log.validate_autho()
	response=addmod.do_ad()
	if response['result']==True:
		redirect('/admin')
	else:
		return response['error']

    #if log.get_user_level() == 2:
    	#addmod.do_ad()

    #else:
    	#return 'Behörighet saknas!'


'''*****Ta bort annons****'''

@post('/del_ad/<which_ad>')
def del_ad(which_ad):
	log.validate_autho()
	if log.get_user_level() == 2:
		user_logged_in=log.get_user_id_logged_in()
		addmod.erase_ad(which_ad, user_logged_in)
	else:
		return 'Behörighet saknas!'


'''****Studenten kan söka en annons****'''

@post('/sok_annons/<which_ad>')
def apply_for_mission(which_ad):
	log.validate_autho()
	response=addmod.applying_for_mission(which_ad)
	if response['result']==True:
		redirect('/admin')
	else:
		return response['error']


'''
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
'''


'''****Listar de studenter som sökt ett specifik uppdrag***'''

@route('/allMissions')
def list_applied_students():
	log.validate_autho()
	if log.get_user_level() == 2:
		user_id=log.get_user_id_logged_in()
		username=log.get_user_name()
		relevant_adds=addmod.get_my_ads(user_id)
		students_application = addmod.students_that_applied(user_id)
		feedback_info = addmod.get_given_feedback_for_employers(user_id)

		return template('adds.tpl',user_id=user_id, user=username, adds=relevant_adds, students=students_application, pageTitle='Alla uppdrag', feedback = feedback_info)


		'''if len(relevant_adds)>0:
			open_ad=addmod.choose_ad(5)
			return template('adds.tpl',user_id=user_id, user=username, adds=relevant_adds, students=students, open_ad=open_ad, pageTitle='Alla uppdrag')
		else:
			open_ad=0
			return template('adds.tpl',user_id=user_id, user=username, adds=relevant_adds, students=students, open_ad=open_ad, pageTitle='Alla uppdrag')'''
	else:
		return "Du har ej behörighet"


@route('/select_student/<annons>/<sokandeID>')
def accepted_ones(annons, sokandeID):
	addmod.who_got_accepted(annons, sokandeID)
	redirect ('/allMissions')


@route('/ad_done/<annons>', method="POST")
def ad_done(annons):
	log.validate_autho()
	if log.get_user_level() == 2:
		response = addmod.move_ad_to_complete(int(annons))
		if response['response'] == False:
			return response['error']
		else:
			redirect('/allMissions')
	else:
		return 'Behörighet saknas!'


@route('/give_feedback/<ad_nr>')
def give_feedback(ad_nr):
	username = log.get_user_name()
	return template('feedback', adnr=ad_nr, pageTitle = 'Ge feedback', user=username )



'''********Övriga Routes********'''

@error(404)
def error404(error):
    return template('pagenotfound', pageTitle = 'Fel!' )

@route('/static/<filename:path>')
def server_static(filename):
	return static_file(filename, root="static")


app = SessionMiddleware(app(), log.session_opts)
run(app=app)
