# *-* coding:utf-8 *-*

'''
*******Creator*******
Se varje funktion
'''


from bottle import request
import log
import MySQLdb
import os.path
import random, string


'''*********Ad validators*********'''

def validate_ad_input(ad_info):
    #Skriven av: Jari
    '''Last point of validation to check that it exists a title'''
    s=list(ad_info)

    if not ad_info:
        return False
    elif s[0]==' ':
        s[0]=''
        ad_info=''.join(s)
        return validate_ad_input(ad_info)
    else:
        return True


'''*********General ad info*********'''

def get_ad_creator_id(cursor, ad_nr):
    #Skriven av: Jari
    ''' Return id of ads creator'''
    sql= "SELECT creator_id FROM ads WHERE id=%s"
    cursor.execute(sql, (ad_nr,))
    mighty_db_says = cursor.fetchall()
    print mighty_db_says[0][0]
    return mighty_db_says[0][0]

def get_my_ads(employers_id, cursor):
    #Skriven av: Jari
    ''' Return a logged-in employers ads'''
    sql= "SELECT id, titel, main_info, creator_id, DATE(creation_date) FROM ads WHERE %s=ads.creator_id"
    cursor.execute(sql, (employers_id,))
    mighty_db_says = cursor.fetchall()
    return mighty_db_says


'''*********Create/remove AD*********'''
def do_ad(cursor):
    #Skriven av: Jari
    '''Get data from user and create an ad'''
    ad_title=request.forms.get('ad_title')
    ad_text=request.forms.get('ad_text')

    ad_title_checked=validate_ad_input(ad_title)
    if  ad_title_checked == True:
        creator = log.get_user_id_logged_in()
        sql="INSERT INTO ads(titel, main_info, creator_id, creation_date)\
        VALUES (%s, %s, %s, CURDATE())"
        cursor.execute(sql, (ad_title, ad_text, creator,))
        return {'result':True, 'error':'None'}

    else:
        return {'result':False, 'error': "Ett fel uppstod - Kontrollera att du gav annonsen en titel"}

def erase_ad(ad_id, user_ID, cursor):
    #Skriven av: Jari
    #Uppdaterad av: Jacob (flytt till sql)
    '''Deletes an ad from DB based on userinput data'''
    ad_id = int(ad_id)
    user_ID = int(user_ID)
    sql="INSERT INTO removed_ads(student_id, titel) \
    SELECT application.student_id, ads.titel FROM application \
    INNER JOIN ads \
    ON application.ad_id = ads.id \
    WHERE application.ad_id = %s"
    cursor.execute(sql, (ad_id,))

    sql= "DELETE FROM application WHERE ad_id = %s"
    cursor.execute(sql, (ad_id,))

    sql= "DELETE FROM ads WHERE id = %s and creator_id=%s"
    cursor.execute(sql, (ad_id, user_ID,))


'''*********AD listing*********'''

def sort_by_status(user, cursor):
    #Skriven av: Jari
    #Mindre uppdateringar av: Jacob
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
                WHERE student_id=%s)\
                as H1\
        WHERE H1.status='Obehandlad' OR H1.status='Vald' OR H1.status='Avslutad' OR H1.status='Bortvald' ORDER BY status"

    cursor.execute(sql, (user,))
    mighty_db_says = cursor.fetchall()
    return mighty_db_says


def available_ads(user, cursor):
    #Skriven av: Jari & Jacob (Parprogrammering)
    '''List the ads which a student have not applied on'''
    sql="SELECT ads.id, ads.titel, ads.main_info, DATE(ads.creation_date), employers.company_name, employers.id as emp_id, application.student_id, application.status\
        FROM ads\
        JOIN employers\
            ON employers.id=ads.creator_id\
        LEFT JOIN application\
            ON ads.id=application.ad_id\
        WHERE ads.id NOT IN\
            (SELECT ad_id FROM application WHERE status = 'Vald' OR status = 'Avslutad' OR student_id =%s GROUP BY ad_id)\
        GROUP BY ads.id"
    cursor.execute(sql, (user,))
    mighty_db_says = cursor.fetchall()
    return mighty_db_says

def get_denied_missions(user, cursor):
    #Skriven av: Jacob
    '''Returns all missions that student did not get.'''
    user = int(user)
    sql="SELECT A.titel \
    FROM (SELECT ads.titel \
        FROM application INNER JOIN ads \
        ON ads.id=application.ad_id \
        WHERE application.status='Bortvald' AND application.student_id = %s) as A \
    UNION \
    SELECT removed_ads.titel \
    FROM removed_ads \
    WHERE student_id = %s"
    cursor.execute(sql, (user, user,))
    mighty_db_says = cursor.fetchall()
    return mighty_db_says

def students_that_applied(user_id, cursor):
    #Skriven av: Jari & Jacob (Parprogrammering)
    '''Returns all studetns that applied on each of employers mission'''
    user_id = int(user_id)
    sql = "SELECT students.id, students.first_name, students.last_name, J1.ad_id, J1.status, education.titel, education.year, users.mail\
    FROM (SELECT student_id, ad_id, status \
            FROM ads \
            INNER JOIN application \
            ON application.ad_id=ads.id \
            WHERE creator_id = %s) as J1 \
    INNER JOIN students \
    ON J1.student_id = students.id \
    INNER JOIN education\
    ON students.education_id = education.education_id and students.education_year = education.year\
    INNER JOIN users\
    ON users.id=J1.student_id"
    cursor.execute(sql, (user_id,))
    mighty_db_says = cursor.fetchall()
    return mighty_db_says

def grading_ads(user, cursor):
    #Skriven av: Jacob
    '''Returns all ads that studetn has completed'''
    user = int(user)
    sql= "SELECT employers.company_name, J2.*\
        FROM \
            (SELECT creator_id, feedback.* \
            FROM (SELECT ads.titel, creator_id, ad_id \
               FROM ads \
               INNER JOIN application \
               ON application.ad_id=ads.id \
               WHERE student_id = %s and status = 'Avslutad') as J1 \
               INNER JOIN feedback \
                ON J1.ad_id = feedback.ad_id) as J2 \
        INNER JOIN employers \
        ON J2.creator_id = employers.id"
    cursor.execute(sql,(user,))
    mighty_db_says = cursor.fetchall()
    return mighty_db_says




'''******Application manegment*****'''
def applying_for_mission(which_ad, cursor):
    #Skriven av: Jari
    #Uppdateringar: Jacob (flytt till sql)
    '''Create an application in the DB on a specifik ad'''
    which_ad=int(which_ad)
    user=log.get_user_id_logged_in()
    ads_user_applied_on=applied_on(user, 'Obehandlad', which_ad, cursor)

    if len(ads_user_applied_on)>0:
        return {'result':False, 'error':'Du har redan ansökt på denna annons!'}
    else:
        sql="INSERT INTO application(ad_id, student_id, status)\
            VALUES (%s, %s, 'Obehandlad')"
        cursor.execute(sql,(which_ad, user,))
        return {'result':True, 'error':None}

def applied_on(who, status, which_ad_id, cursor):
    #Skriven av: Jari
    '''Check that the student have not applied before on a specifik ad'''
    if which_ad_id==None:
        sql="SELECT * FROM application WHERE %s=application.student_id \
        AND application.status=%s"
        cursor.execute(sql, (who, status,))
    else:
        sql="SELECT * FROM application WHERE %s=application.student_id \
        AND application.status=%s AND application.ad_id=%s"
        cursor.execute(sql,(who, status, which_ad_id,))
    mighty_db_says = cursor.fetchall()
    return mighty_db_says


def who_got_accepted(annons, sokandeID, cursor):
    #Skriven av: Jari
    #Uppdaeringar av: Jacob (flytt till sql)
    '''An application is accepted. The remainding applications status is change to Bortvald'''
    log.validate_autho()
    user=log.get_user_id_logged_in()
    annons = int(annons)
    sokandeID = int(sokandeID)
    sql = "UPDATE application SET status = 'Bortvald' where ad_id=%s"
    cursor.execute(sql,(annons,))

    sql = "UPDATE application SET status = 'Vald' where ad_id=%s and student_id = %s"
    cursor.execute(sql, (annons, sokandeID,))



'''**************Feedback section**************'''
    #Skriven av: Jacob
def move_ad_to_complete(annons, cursor):
    '''Change status on ad and gives feedback to student'''
    feedback = request.forms.get('feedback')
    grade = int(request.forms.get('grade'))
    if feedback == None or len(feedback) == 0:
        return {'response':False, 'error':'Du måste skriva något!'}

    else:
        annons = int(annons)
        employer = log.get_user_id_logged_in()
        sql="SELECT creator_id FROM ads WHERE id = %s"
        cursor.execute(sql, (annons,))
        mighty_db_says_about_employer = cursor.fetchall()

        sql="SELECT student_id FROM application WHERE status = 'Vald' and ad_id=%s"
        cursor.execute(sql, (annons,))
        mighty_db_says_about_status = cursor.fetchall()

        if mighty_db_says_about_employer[0][0] == int(employer) and len(mighty_db_says_about_status) == 1:
            sql="INSERT INTO feedback(ad_id, display, feedback_text, grade) \
            VALUES(%s, %s, %s, %s)"
            cursor.execute(sql, (annons, 1, feedback, grade,))

            sql = "UPDATE application SET status = 'Avslutad' WHERE ad_id=%s AND status='Vald'"
            cursor.execute(sql, (annons,))

            sql = "UPDATE application SET status = 'Bortvald' WHERE ad_id=%s AND status='Obehandlad'"
            cursor.execute(sql, (annons,))

            return {'response':True}

        else:
            return {'response':False, 'error':'Något har blivit fel!'}



def get_given_feedback_for_employers(user, cursor):
    #Skriven av: Jacob
    sql = "SELECT J1.id, feedback.feedback_text, feedback.grade \
        FROM (SELECT ads.titel, ads.id \
            FROM ads \
            INNER JOIN employers \
            ON employers.id=ads.creator_id \
            WHERE employers.id = %s) as J1 \
                INNER JOIN feedback \
                ON J1.id = feedback.ad_id"
    cursor.execute(sql, (user,))
    mighty_db_says = cursor.fetchall()
    return mighty_db_says


def edit_mission(ad_id, cursor):
    #Skriven av: Jacob
    '''Handle edit by students on completed missions that displays on profile'''
    type_of = request.forms.get('mission_type_'+str(ad_id))
    keys = request.POST.getall("add_key_" + str(ad_id))
    display = request.forms.get('display_'+str(ad_id))
    upload  = request.files.get('fileToUpload_'+str(ad_id))

    #Image handeling
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
    #Image handeling - END

    if upload == None:
        sql="UPDATE feedback SET display=%s, url_demo =%s, type=%s WHERE ad_id = %s"
        cursor.execute(sql, (to_display, url, type_of, ad_id,))
    else:
        sql="UPDATE feedback SET img_url =%s, display=%s, url_demo =%s, type=%s WHERE ad_id = %s"
        cursor.execute(sql, (file_path,to_display, url, type_of,ad_id,))

    sql = "DELETE FROM ad_skills WHERE ad_id = %s"
    cursor.execute(sql, (ad_id,))

    #Skills handeling
    keys = zip(keys)
    sql = "INSERT INTO skills (name) \
    VALUES (%s) \
    ON DUPLICATE KEY UPDATE name = name;"
    cursor.executemany(sql, keys)

    new_keys = []
    for key in keys:
        key = list(key)
        key.append(int(ad_id))
        new_keys.append(tuple(key))
    sql = "INSERT INTO ad_skills (skill, ad_id) \
    VALUES ((select name from skills where name = (%s)), (select id from ads where id = (%s)))"
    cursor.executemany(sql, new_keys)
    #Skills handeling - END

def get_ad_skills(user, cursor):
    #Skriven av: Jacob
    '''Returns all skills needed for each ad'''
    user = int(user)
    sql="SELECT ad_skills.* \
    FROM (SELECT ad_id FROM application WHERE student_id=%s AND status = 'Avslutad') as J \
    JOIN ad_skills \
    ON ad_skills.ad_id = J.ad_id"
    cursor.execute(sql, (user,))
    mighty_db_says = cursor.fetchall()
    return mighty_db_says
