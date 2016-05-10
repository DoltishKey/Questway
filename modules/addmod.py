# *-* coding:utf-8 *-*
from bottle import request, redirect
import log
import createUsers
import MySQLdb
import os.path
import random, string


'''*********DB info*********'''

def call_database(sql, asked_from_cursor):
    db = MySQLdb.connect(host="195.178.232.16", port=3306, user="AC8240", passwd="hejhej123", db="AC8240");
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


'''*********Create the AD*********'''
def do_ad():
    ad_title=request.forms.get('ad_title')
    ad_text=request.forms.get('ad_text')

    ad_title_checked=validate_ad_input(ad_title)
    if  ad_title_checked == True:
        creator = log.get_user_id_logged_in()
        sql="INSERT INTO ads(titel, main_info, creator_id, creation_date)\
        VALUES ('%s', '%s', '%d', CURDATE())" % (ad_title, ad_text, creator)

        ask_it_to = []
        mighty_db_says = call_database(sql, ask_it_to)
        return {'result':True, 'error':'None'}

    else:
        return {'result':False, 'error': "Ett fel uppstod - Kontrollera att du gav annonsen en titel"}


'''*********Check that a Title for the ad is given*********'''

def validate_ad_input(ad_info):
    '''Last point of validation that it exists a title'''
    s=list(ad_info)

    if not ad_info:
        return False
    elif s[0]==' ':
        s[0]=''
        ad_info=''.join(s)
        return validate_ad_input(ad_info)
    else:
        return True


'''*********Check and manage Ads*********'''

def get_my_ads(employers_id):
    ''' Return a logged-in employers ads'''
    sql= "SELECT id, titel, main_info, creator_id, DATE(creation_date) FROM ads WHERE '%d'=ads.creator_id" %(employers_id)

    ask_it_to = ['fetchall()']
    mighty_db_says = call_database(sql, ask_it_to)
    return mighty_db_says[0]


def sort_by_status(user):
    '''List the ads relevant for a specifik user'''
    sql="SELECT * FROM\
			    (SELECT ads.id, ads.titel, ads.main_info, DATE(ads.creation_date), employers.company_name, employers.id as emp_id,\
                application.student_id, application.status, employers.first_name, employers.last_name, users.mail, feedback.feedback_text, feedback.grade\
			    FROM ads\
			    JOIN employers\
			        ON ads.creator_id=employers.id\
                JOIN users\
                    ON employers.id = users.id\
			    LEFT JOIN application\
			        ON ads.id=application.ad_id\
                LEFT JOIN feedback\
                    ON application.ad_id = feedback.ad_id AND application.status = 'Avslutad'\
                WHERE student_id='%d')\
		        as H1\
        WHERE H1.status='Obehandlad' OR H1.status='Vald' OR H1.status='Avslutad' OR H1.status='Bortvald' ORDER BY status" %(user)

    ask_it_to = ['fetchall()']
    mighty_db_says = call_database(sql, ask_it_to)
    the_ads=mighty_db_says[0]
    return the_ads


def available_ads(user):
    '''List the ads which a student have not applied on'''
    sql="SELECT ads.id, ads.titel, ads.main_info, DATE(ads.creation_date), employers.company_name, employers.id as emp_id, application.student_id, application.status\
        FROM ads\
        JOIN employers\
            ON employers.id=ads.creator_id\
        LEFT JOIN application\
            ON ads.id=application.ad_id\
        WHERE ads.id NOT IN\
            (SELECT ad_id FROM application WHERE status = 'Vald' OR status = 'Avslutad' OR student_id ='%d' GROUP BY ad_id)\
        GROUP BY ads.id" % (user)

    ask_it_to = ['fetchall()']
    mighty_db_says = call_database(sql, ask_it_to)
    the_ads=mighty_db_says[0]
    return the_ads


'''******* Delete a specifik ad *******'''

def erase_ad(ad_id, user_ID):
    ad_id = int(ad_id)
    sql="INSERT INTO removed_ads(student_id, titel) \
    SELECT application.student_id, ads.titel FROM application \
    INNER JOIN ads \
    ON application.ad_id = ads.id \
    WHERE application.ad_id = '%d'"%(ad_id)

    ask_it_to = []
    mighty_db_says = call_database(sql, ask_it_to)

    sql= "DELETE FROM application WHERE ad_id = '%d'" %(int(ad_id))
    ask_it_to = []
    mighty_db_says = call_database(sql, ask_it_to)

    sql= "DELETE FROM ads WHERE id = '%d' and creator_id='%d'" %(int(ad_id), int(user_ID))
    ask_it_to = []
    mighty_db_says = call_database(sql, ask_it_to)

    redirect('/allMissions')


'''*****Which ads student applied on****'''
def applied_on(who, status, which_ad_id):
    '''Check that the student have not applied before on a specifik ad'''
    if which_ad_id==None:
        sql="SELECT * FROM application WHERE '%d'=application.student_id \
        AND application.status='%s'" %(who, status)
    else:
        sql="SELECT * FROM application WHERE '%d'=application.student_id \
        AND application.status='%s' AND application.ad_id='%d'" %(who, status, which_ad_id)

    ask_it_to = ['fetchall()']
    mighty_db_says = call_database(sql, ask_it_to)
    return mighty_db_says[0]

'''****** Student Applying on ad *****'''
def applying_for_mission(which_ad):
    '''Create an application in the DB on a specifik ad'''
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
    '''An application is accepted. The remainding applications status is change to Bortvald'''
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
        mighty_db_says_about_employer = call_database(sql, ask_it_to)

        sql="SELECT student_id FROM application WHERE status = 'Vald'"
        ask_it_to = ['fetchall()']
        mighty_db_says_about_status = call_database(sql, ask_it_to)

        if mighty_db_says_about_employer[0][0][0] == int(employer) and len(mighty_db_says_about_status[0]) == 1:
            sql="INSERT INTO feedback(ad_id, display, feedback_text, grade) \
            VALUES('%d', '%d', '%s', '%d')"%(annons, 1, feedback, grade)
            ask_it_to = []
            call_database(sql, ask_it_to)

            sql = "UPDATE application SET status = 'Avslutad' WHERE ad_id='%d' AND status='Vald'"%(annons)
            ask_it_to = []
            call_database(sql, ask_it_to)

            sql = "UPDATE application SET status = 'Bortvald' WHERE ad_id='%d' AND status='Obehandlad'"%(annons)
            ask_it_to = []
            call_database(sql, ask_it_to)

            return {'response':True}

        else:
            return {'response':False, 'error':'Något har blivit fel!'}


def edit_mission(ad_id):
    type_of = request.forms.get('mission_type_'+str(ad_id))
    keys = request.POST.getall("add_key_" + str(ad_id))
    display = request.forms.get('display_'+str(ad_id))
    upload  = request.files.get('fileToUpload_'+str(ad_id))
    if upload != None:
        name, ext = os.path.splitext(upload.filename)
        if ext not in ('.png','.jpg','.jpeg'):
            return 'File extension not allowed.'

        save_path = "static/img/uploads"
        upload.filename = str(''.join(random.choice(string.lowercase + string.digits) for i in range(16)))+str(ext)
        while os.path.isfile('static/img/uploads/' + upload.filename) == True:
            upload.filename = str(''.join(random.choice(string.lowercase + string.digits) for i in range(16)))+str(ext)

        print upload.filename
        file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
        upload.save(file_path)

    if display == 'True':
        to_display = 2
    else:
        to_display = 1
    url = request.forms.get('url_'+str(ad_id))
    ad_id = int(ad_id)
    if upload == None:
        sql="UPDATE feedback SET display='%d', url_demo ='%s', type='%s' WHERE ad_id = '%d'"%(to_display, url, type_of,ad_id)

    else:
        sql="UPDATE feedback SET img_url ='%s', display='%d', url_demo ='%s', type='%s' WHERE ad_id = '%d'"%(file_path,to_display, url, type_of,ad_id)

    ask_it_to = []
    call_database(sql, ask_it_to)

    ask_it_to = []
    sql = "DELETE FROM ad_skills WHERE ad_id = '%d'"%(ad_id)
    call_database(sql, ask_it_to)

    for key in keys:
        ask_it_to = []
        sql = "INSERT INTO skills (name) \
        VALUES ('%s') \
        ON DUPLICATE KEY UPDATE name = name;"%(key)
        call_database(sql, ask_it_to)

        ask_it_to = []
        sql = "INSERT INTO ad_skills (skill, ad_id) \
        VALUES ((select name from skills where name = '%s'), (select id from ads where id = '%d'))"%(key, ad_id )
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
	return mighty_db_says[0]



def students_that_applied(user_id):
	user_id = int(user_id)
	sql = "SELECT students.id, students.first_name, students.last_name, J1.ad_id, J1.status, education.titel, education.year, users.mail\
	FROM (SELECT student_id, ad_id, status \
			FROM ads \
			INNER JOIN application \
			ON application.ad_id=ads.id \
			WHERE creator_id = '%d') as J1 \
	INNER JOIN students \
	ON J1.student_id = students.id \
    INNER JOIN education\
    ON students.education_id = education.education_id and students.education_year = education.year\
    INNER JOIN users\
    ON users.id=J1.student_id"%(user_id)

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


def get_denied_missions(user):
    user = int(user)
    sql="SELECT A.titel \
    FROM (SELECT ads.titel \
        FROM application INNER JOIN ads \
        ON ads.id=application.ad_id \
        WHERE application.status='Bortvald' AND application.student_id = '%d') as A \
    UNION \
    SELECT removed_ads.titel \
    FROM removed_ads \
    WHERE student_id = '%d'"%(user, user)
    ask_it_to = ['fetchall()']
    mighty_db_says = call_database(sql, ask_it_to)
    return mighty_db_says[0]

def get_ad_skills(user):
    sql="SELECT ad_skills.* \
    FROM (SELECT ad_id FROM application WHERE student_id='%d' AND status = 'Avslutad') as J \
    JOIN ad_skills \
    ON ad_skills.ad_id = J.ad_id"%(int(user))
    ask_it_to = ['fetchall()']
    mighty_db_says = call_database(sql, ask_it_to)
    return mighty_db_says[0]
