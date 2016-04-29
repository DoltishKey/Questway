# *-* coding:utf-8 *-*
import json
from bottle import request, redirect, static_file
import time
import log
import createUsers
import MySQLdb
import os


'''*********DB info*********'''
def call_database(sql, asked_from_cursor):
    db = MySQLdb.connect(host="195.178.232.7", port=4040, user="AC8240", passwd="hejhej123", db="AC8240");
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



'''*********Skriv/läsa filer*********'''
def read_data(file):
	try:
		fileIn = open('static/data/'+ file +'.json', 'r')
		dataRead = json.load(fileIn)
		fileIn.close()
	except (IOError, ValueError):
		validatekDataFile(file)
		dataRead = read_data(file)
	return dataRead

def write_to_db(users, db):
	fileOut = open('static/data/'+ db +'.json', 'w')
	json.dump(users, fileOut, indent=4)
	fileOut.close()

def validatekDataFile(file):
	'''Om databasen inte finns eller är helt tom så skapas en json-fil innehållande en tom lista.'''
	resList = []
	dataFile = open('static/data/'+ file +'.json', 'w')
	json.dump(resList, dataFile, indent=4)
	dataFile.close()



'''*********Load adds from DB. If there's not DB, one is created*********'''

def load_adds(file):
    try:
        with open('static/data/ads.json', "r") as fil:
            data=json.load(fil)
            return data

    except (ValueError, IOError):
        data=create_ad_DB()
        return data

def create_ad_DB():
    with open('static/data/ads.json', 'w') as fil:
        data=[]
        json.dump(data, fil, indent=4)
        return data


'''*********Create the AD*********'''
def do_ad():
	#mydict={}
	#mylist=['ad_title', 'ad_text']
	ad_title=request.forms.get('ad_title')
	ad_text=request.forms.get('ad_text')

	'''
	for i in mylist:
		j=request.forms.get(i)
		mydict.update({i:j})
	'''

	#ad_title_checked=check_ad_info(ad_title)
	ad_title_checked = True
	if  ad_title_checked == True:
		#date_ad_created=time.strftime('%d/%m/%Y')
		#uniq_number=1
		#ad_ID=check_adID(uniq_number)
		creator = log.get_user_id_logged_in()
		#mydict.update({'uniq_adNr':ad_ID, 'status':'Ingen vald', 'who_applied':[], 'creator':creator, 'date_of_adcreation':date_ad_created, 'the_chosen_one':''})

		#content=load_adds('ads')
		#content.append(mydict)

		sql="INSERT INTO ads(titel, main_info, creator_id, creation_date)\
			VALUES ('%s', '%s', '%d', CURDATE())" % (ad_title, ad_text, creator)

		ask_it_to = []
		mighty_db_says = call_database(sql, ask_it_to)
		return {'result':True, 'error':'None'}

		'''
		with open('static/data/ads.json', "w") as fil:
			json.dump(content, fil, indent=4)
		'''

	else:
		return {'result':False, 'error': "Ett fel uppstod - Kontrollera att du gav annonsen en titel"}


'''*********Check that a Title for the ad is given*********'''

def check_ad_info(ad_info): #Byt namn på variabeln till validate_ad_input
    former_ad_info=load_adds('ads')
    s=list(ad_info)

    if not ad_info:
        return False
    elif s[0]==' ':
        s[0]=''
        ad_info=''.join(s)
        return check_ad_info(ad_info)
    elif len(former_ad_info)==0:
        return True
    else:
        return True


'''*********Check and manage Ads ID*********'''

def check_adID(number):
    all_adds=load_adds('ads')
    for each in all_adds:
        if each['uniq_adNr']==number:
            number+=1
            return check_adID(number)
    return number

def get_my_ads(employers_id):
	sql= "SELECT id, titel, main_info, creator_id, DATE(creation_date) FROM ads WHERE '%d'=ads.creator_id" %(employers_id)

	ask_it_to = ['fetchall()']
	mighty_db_says = call_database(sql, ask_it_to)
	return mighty_db_says[0]

'''**********Pair employers to their ads************'''
def join_ads_employers():
	sql="SELECT employers.company_name, ads.titel, ads.main_info, employers.id, DATE(ads.creation_date), ads.id \
	FROM ads \
	INNER JOIN employers \
	ON employers.id=ads.creator_id"

	ask_it_to = ['fetchall()']
	mighty_db_says = call_database(sql, ask_it_to)
	joined_employers_ads=mighty_db_says[0]

	return joined_employers_ads


'''******* Delete a specifik ad *******'''
def erase_ad(ad_id, user_ID):
	sql= "DELETE FROM ads WHERE id = '%d' and creator_id='%d'" %(int(ad_id), int(user_ID))
	ask_it_to = []
	mighty_db_says = call_database(sql, ask_it_to)

	redirect('/allMissions')


def choose_ad(annonsID):
	sql= "SELECT * FROM ads WHERE id='%d'" %(annonsID)
	ask_it_to = ['fetchall()']
	mighty_db_says = call_database(sql, ask_it_to)
	return mighty_db_says[0]

'''*****Which ads student applied on****'''
def applied_on(who, status, which_ad_id):
	if which_ad_id==None:
		print "nej"
		sql="SELECT * FROM application WHERE '%d'=application.student_id \
		AND application.status='%s'" %(who, status)
	else:
		print "ja"
		sql="SELECT * FROM application WHERE '%d'=application.student_id \
		AND application.status='%s' AND application.ad_id='%d'" %(who, status, which_ad_id)

	ask_it_to = ['fetchall()']
	mighty_db_says = call_database(sql, ask_it_to)
	return mighty_db_says[0]

'''****** Student Applying on ad *****'''
def applying_for_mission(which_ad):
	log.validate_autho()
	which_ad=int(which_ad)
	user=log.get_user_id_logged_in()
	ads_user_applied_on=applied_on(user, 'Obehandlad', which_ad)

	if len(ads_user_applied_on)>0:
		return {'result':False, 'error':'Du har redan ansökt på denna annons!'}
	else:
		sql="INSERT INTO application(ad_id, student_id, status)\
			VALUES ('%d', '%d', '%s')" % (which_ad, user, 'Obehandlad')
		ask_it_to = []
		mighty_db_says = call_database(sql, ask_it_to)
		return {'result':True, 'error':None}



'''*********Choose a Student********'''
def who_got_accepted(annons, sokandeID):
	log.validate_autho()
	user=log.get_user_id_logged_in()
	annons = int(annons)
	sokandeID = int(sokandeID)
	sql = "UPDATE application SET status = 'Bortvald' where ad_id='%d'"%(annons)
	ask_it_to = []
	mighty_db_says = call_database(sql, ask_it_to)

	sql = "UPDATE application SET status = 'Vald' where ad_id='%d' and student_id = '%d'"%(annons, sokandeID)
	ask_it_to = []
	mighty_db_says = call_database(sql, ask_it_to)


'''********My list of ads*********'''
def my_ads(userID):
	userID = int(userID)
	sql = "SELECT * FROM ads WHERE creator_id = '%d'"%(userID)
	ask_it_to = ['fetchall()']
	mighty_db_says = call_database(sql, ask_it_to)
	return mighty_db_says[0]


'''*********Moves AD to Done*********'''
def move_ad_to_complete(annons):
	feedback = request.forms.get('feedback')
	grade = int(request.forms.get('grade'))
	if feedback == None or len(feedback) == 0:
		return {'response':False, 'error':'Du måste skriva något!'}

	else:

		annons = int(annons)
		employer = log.get_user_id_logged_in()
		sql="SELECT creator_id FROM ads WHERE id = '%d'"%(annons)
		ask_it_to = ['fetchall()']
		mighty_db_says = call_database(sql, ask_it_to)

		mighty_db_says[0][0][0]

		if mighty_db_says[0][0][0] == int(employer):
			sql="INSERT INTO feedback(ad_id, display, feedback_text, grade) \
			VALUES('%d', '%d', '%s', '%d')"%(annons, 1, feedback, grade)
			ask_it_to = []
			call_database(sql, ask_it_to)

			sql = "UPDATE application SET status = 'Avslutad' WHERE ad_id='%d' AND status='Vald'"%(annons)
			ask_it_to = []
			call_database(sql, ask_it_to)
			return {'response':True}

		else:
			return {'response':False, 'error':'Något har blivit fel!'}

def ajax_edit_mission():
    type_of = request.forms.get('mission_type')
    keys = request.POST.getall("add_key")
    display = request.forms.get('display')
    upload  = request.files.get('fileToUpload')
    print upload
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'

    save_path = '/static/img/'
    upload.save(save_path) # appends upload.filename automatically
    return 'OK'


    if display == 'True':
        print 'Komemr hit!'
        to_display = 2
    else:
        to_display = 1
    url = request.forms.get('url')
    grading_id = int(request.forms.get('grading_id'))

    sql="UPDATE feedback SET display='%d', url_demo ='%s', type='%s' WHERE ad_id = '%d'"%(to_display, url, type_of,grading_id)
    ask_it_to = []
    call_database(sql, ask_it_to)




def grading_ads(user):
	sql= "SELECT employers.company_name, J2.*\
	    FROM \
	        (SELECT creator_id, feedback.* \
	        	FROM (SELECT ads.titel, creator_id, ad_id \
	        			FROM ads \
	        			INNER JOIN application \
	        			ON application.ad_id=ads.id \
	        			WHERE student_id = '%d' and status = 'Avslutad') as J1 \
	        	INNER JOIN feedback \
	        	ON J1.ad_id = feedback.ad_id) as J2 \
	    INNER JOIN employers \
	    ON J2.creator_id = employers.id"%(user)

	ask_it_to = ['fetchall()']
	mighty_db_says = call_database(sql, ask_it_to)
	print mighty_db_says[0]
	return mighty_db_says[0]

def students_that_applied(user_id):
	user_id = int(user_id)
	sql = "SELECT students.id, students.first_name, students.last_name, J1.ad_id, J1.status\
	FROM (SELECT student_id, ad_id, status \
			FROM ads \
			INNER JOIN application \
			ON application.ad_id=ads.id \
			WHERE creator_id = '%d') as J1 \
	INNER JOIN students \
	ON J1.student_id = students.id"%(user_id)

	ask_it_to = ['fetchall()']
	mighty_db_says = call_database(sql, ask_it_to)
	return mighty_db_says[0]

def get_given_feedback_for_employers(user):
    sql = "SELECT J1.id, feedback.feedback_text, feedback.grade \
	           FROM (SELECT ads.titel, ads.id \
	              FROM ads \
	                 INNER JOIN employers \
	                    ON employers.id=ads.creator_id \
	                       WHERE employers.id = '%d') as J1 \
	            INNER JOIN feedback \
	        ON J1.id = feedback.ad_id"%(user)

    ask_it_to = ['fetchall()']
    mighty_db_says = call_database(sql, ask_it_to)
    return mighty_db_says[0]
