# *-* coding:utf-8 *-*
import json
from bottle import request, redirect 
import time
import log
import createUsers


    
    
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
        mydict.update({'uniq_adNr':ad_ID, 'status':'Ingen vald', 'who_applied':[], 'creator':creator, 'date_of_adcreation':date_ad_created})
        
        content=load_adds('ads')
        content.append(mydict)
        with open('static/data/ads.json', "w") as fil:
            json.dump(content, fil, indent=4)
        redirect('/showadds')
    
    else:
        redirect('/showadds')
        

'''*********Check that a Title for the ad is given*********'''

def check_ad_info(ad_info):
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
        if int(each['uniq_adNr']) == int(annonsID) and str(each['status'])==str(status):
            return each
        