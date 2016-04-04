# *-* coding:utf-8 *-*
import json


'''*********Managing ads from Database*********'''

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

'''
def check_ad_info(adinfo):
    former_ad_info=load_adds('ads')
        
    if len(former_ad_info)==0:
        return True
        
    boolval=True
    for eachadd in former_ad_info:
        if eachadd['ad_title'] == adinfo:
            boolval=False
        elif boolval==False:
            return False
        else:
            boolval=True
    return boolval
'''


'''*********Check and manage Ads ID*********'''

def check_adID(number):
    all_adds=load_adds('ads')
    for each in all_adds:
        if each['uniq_adNr']==number:
            number+=1
            return check_adID(number)
    return number