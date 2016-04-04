# *-* coding:utf-8 *-*
import json
from bottle import request, redirect 
import time



        
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
    
    
'''*********Create the ad*********'''
def do_ad():
    checkAdinfo=False
    mydict={}
    mylist=['ad_title', 'ad_text', 'ad_orgNr', 'ad_corpName']
    for i in mylist:
        j=request.forms.get(i)
        mydict.update({i:j})
        
    content=load_adds('ads')
    checkAdinfo=check_ad_info(mydict['ad_title'])
    
    if checkAdinfo == True:
        date_ad_created=time.strftime('%d/%m/%Y')
        uniq_number=1
        ad_ID=check_adID(uniq_number)
        mydict.update({'uniq_adNr':ad_ID, 'status':'', 'who_applied':[], 'creator':'', 'date_of_adcreation':date_ad_created})
        
        content.append(mydict)
        with open('static/data/ads.json', "w") as fil:
            json.dump(content, fil, indent=4)
        redirect('/showadds')
    
    else:
        redirect('/showadds')
        

'''*********Check that an Title for the ad is given*********'''

def check_ad_info(ad_info):
    former_ad_info=load_adds('ads')
    
    if not ad_info:
        return False
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