# *-* coding:utf-8 *-*
import json
from bottle import request, redirect
import time
import log
import createUsers



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
    mydict={}
    mylist=['ad_title', 'ad_text']
    for i in mylist:
        j=request.forms.get(i)
        mydict.update({i:j})

    checkAdinfo=check_ad_info(mydict['ad_title'])

    if checkAdinfo == True:
        date_ad_created=time.strftime('%d/%m/%Y')
        uniq_number=1
        ad_ID=check_adID(uniq_number)
        creator = log.get_user_id_logged_in()
        mydict.update({'uniq_adNr':ad_ID, 'status':'Ingen vald', 'who_applied':[], 'creator':creator, 'date_of_adcreation':date_ad_created, 'the_chosen_one':''})

        content=load_adds('ads')
        content.append(mydict)
        with open('static/data/ads.json', "w") as fil:
            json.dump(content, fil, indent=4)
        redirect('/admin')

    else:
        return "Ett fel uppstod - Kontrollera att du gav annonsen en titel"


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

def get_corp_name(all_adds):
	corps = createUsers.read_data('employers')
	for add in all_adds:
		for corp in corps:
			if add['creator'] == corp ['id']:
				add.update({'ad_corpName':corp['company_name']})

	return all_adds



'''*********Choose a specific AD*********'''

def choose_ad(annonsID, db, status):
    for each in db:
        if int(each['uniq_adNr']) == int(annonsID) and str(each['the_chosen_one'])==str(status):
            return each
        elif int(each['uniq_adNr']) == int(annonsID) and status==None:
            return each



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
