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
	log.validate_autho() #and log.get_user_level() == 2 | kontrollerar om användaren är inloggad & tar hand om en-inloggade
	username = log.get_user_name() #hämtar användarens namn från DB (returnerar en sträng)
	user_level = log.get_user_level() #kollar om användaren är uppdragstagare eller student (returnerar 1 eller 2)
	if user_level == 1:
		return template('admin', user=username, level="student")
	else:
		return template('admin', user=username, level="arbetsgivare")

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
		redirect('/admin') 
	else:
		return response['error']
		
@route('/do_create_student', method = 'POST')
def do_create_employer():
	response = createUsers.create_student()
	if response['result'] == True:
		redirect('/admin') 
	else:
		return response['error']

@route('/profiles/<user>')
def profiles(user):
	user_profile_data = createUsers.show_student_profile(user)
	if user_profile_data['exists'] == True:
		return template('user_profile', student_id = user)
	
	else:
		return 'Användaren finns inte!'

    
    
'''********Ad-management********'''

@route('/showadds')
def show_adds():
    all_adds=addmod.load_adds('ads')
    return template('adsform.tpl', annons=all_adds)
    

@post('/make_ad')
def ad_done():
    #checkAdinfo=False
    #all_adds=load_adds('ads')
    mydict={}
    mylist=['ad_title', 'ad_text', 'ad_orgNr', 'ad_corpName']
    for i in mylist:
        j=request.forms.get(i)
        mydict.update({i:j})
    
    content=addmod.load_adds('ads')

    uniq_number=1
    adID=addmod.check_adID(uniq_number)
    mydict.update({'uniq_adNr':adID})
        
    content.append(mydict)
    with open('static/data/ads.json', "w") as fil:
        json.dump(content, fil, indent=4)
    redirect('/showadds')

    
@post('/del_ad/<annons>')
def del_ad(annons):
    all_adds=addmod.load_adds('ads')
    for each in all_adds:
        if int(each['uniq_adNr']) == int(annons):
            all_adds.remove(each)
    with open('static//data/ads.json', 'w') as fil:
        json.dump(all_adds, fil, indent=4)
    redirect('/showadds')
    
    
    
'''********Övriga Routes********'''

@error(404)
def error404(error):
    return template('pagenotfound')	
	
@route('/static/<filename:path>')
def server_static(filename):
	return static_file(filename, root="static")


app = SessionMiddleware(app(), log.session_opts)		 	 
run(app=app)		 	 