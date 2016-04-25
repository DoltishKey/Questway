# *-* coding:utf-8 *-*
import json
from bottle import request, redirect
import time
import log
import createUsers
import MySQLdb
db = MySQLdb.connect(host="195.178.232.7", port=4040, user="AC8240", passwd="hejhej123", db="AC8240");
cursor = db.cursor()

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

	ad_title_checked=check_ad_info(ad_title)

	if  ad_title_checked == True:
		#date_ad_created=time.strftime('%d/%m/%Y')
		#uniq_number=1
		#ad_ID=check_adID(uniq_number)
		creator = log.get_user_id_logged_in()
		#mydict.update({'uniq_adNr':ad_ID, 'status':'Ingen vald', 'who_applied':[], 'creator':creator, 'date_of_adcreation':date_ad_created, 'the_chosen_one':''})

		#content=load_adds('ads')
		#content.append(mydict)

		sql_query="INSERT INTO ads(titel, main_info, creator_id, creation_date)\
			VALUES ('%s', '%s', '%d', CURDATE())" % (ad_title, ad_text, creator)

		cursor.execute(sql_query)
		db.commit()
		return {'result':True, 'error':None}

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
	query= "SELECT id, titel, main_info, creator_id, DATE(creation_date) FROM ads WHERE '%d'=ads.creator_id" %(employers_id)

	cursor.execute(query)
	return cursor.fetchall()

'''**********Pair employers to their ads************'''
def join_ads_employers():
	sql_query="SELECT employers.company_name, ads.titel, ads.main_info, employers.id, DATE(ads.creation_date), ads.id \
	FROM ads \
	INNER JOIN employers \
	ON employers.id=ads.creator_id"

	cursor.execute(sql_query)
	joined_employers_ads=cursor.fetchall()

	return joined_employers_ads


'''******* Delete a specifik ad *******'''
def erase_ad(ad_id, user_ID):
	query= "DELETE FROM ads WHERE id = '%d' and creator_id='%d'" %(int(ad_id), int(user_ID))
	cursor.execute(query)
	db.commit()
	redirect('/allMissions')


'''*****Which ads student applied on****'''
def applied_on(who, status):
	query="SELECT * FROM application WHERE '%d'=application.student_id \
	AND application.status='%s'" %(who, status)

	cursor.execute(query)
	return cursor.fetchall()


'''****** Student Applying on ad *****'''
def applying_for_mission(which_ad):
	log.validate_autho()
	which_ad=int(which_ad)
	user=log.get_user_id_logged_in()
	ads_user_applied_on=applied_on(user, 'Obehandlad')

	if len(ads_user_applied_on) > 0:
		return {'result':False, 'error':'Du har redan ansökt på denna annons!'}
	else:
		query="INSERT INTO application(ad_id, student_id, status)\
			VALUES ('%d', '%d', '%s')" % (which_ad, user, 'Obehandlad')
		cursor.execute(query)
		db.commit()
		return {'result':True, 'error':None}


'''*********Choose a specific AD*********'''
def choose_ad(ad_id):
	query= "SELECT * FROM ads WHERE id='%d'" %(ad_id)

	cursor.execute(query)
	return cursor.fetchall()

	'''
    for each in db:
        if int(each['uniq_adNr']) == int(annonsID) and str(each['the_chosen_one'])==str(status):
            return each
        elif int(each['uniq_adNr']) == int(annonsID) and status==None:
            return each
	'''


'''*********Choose a Student********'''
def who_got_accepted(annons, sokandeID):
	all_ads=load_adds('ads')
	user=log.get_user_id_logged_in()

	what_ad=choose_ad(annons, all_ads, None)
	print what_ad
	for who in what_ad['who_applied']:
		for ad in all_ads:
			if int(who)==int(sokandeID) and what_ad['uniq_adNr']==ad['uniq_adNr']:
				print "hey"
				ad.update({'the_chosen_one':int(sokandeID)})
				ad['who_applied'].remove(int(sokandeID))
				print ad
				print all_ads
	with open('static/data/ads.json', 'w') as fil:
		json.dump(all_ads, fil, indent=4)
	redirect ('/allMissions')


'''********My list of ads*********'''
def my_ads(userID):
	all_adds=load_adds('ads')
	relevant_adds=[]
	for add in all_adds:
		if userID == add['creator'] or userID==add['the_chosen_one']:
			relevant_adds.append(add)
	return relevant_adds


'''*********Moves AD to Done*********'''
def move_ad_to_complete(annons):
    feedback = request.forms.get('feedback')
    grade = request.forms.get('grade')
    if feedback == None or len(feedback) == 0:
        return {'response':False, 'error':'Du måste skriva något!'}

    else:
        employer = log.get_user_id_logged_in()
        all_ads = read_data('ads')
        ad = choose_ad(annons, all_ads, 'Student vald')
        if int(employer) == int(ad['creator']) and ad['status'] == 'Student vald':
            ad.update({'feedback':feedback, 'grade':grade,'display':False})
            all_grades = read_data('grading')
            all_grades.append(ad)
            write_to_db(all_grades,'grading')
            for ad_object in all_ads:
                if int(ad_object['uniq_adNr']) == int(annons):
                        all_ads.remove(ad_object)
            write_to_db(all_ads, 'ads')
            return {'response':True}

        else:
            return {'response':False, 'error':'Något har blivit fel!'}

def ajax_edit_mission():
		type_of = request.forms.get('mission_type')
		keys = request.POST.getall("add_key")
		display = request.forms.get('display')
		url = request.forms.get('url')
		grading_id = request.forms.get('grading_id')
		all_grades = read_data('grading')

		for grade in all_grades:
			if int(grade['uniq_adNr']) == int(grading_id):
				for key in keys:
					grade['keys'].append(key)
				grade['url'] = url
				grade['display'] = display
				grade['type'] = type_of

		write_to_db(all_grades,'grading')
