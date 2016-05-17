#import unittest
import MySQLdb
from addmod import validate_ad_input, do_ad, sort_by_status
from log import validate_user

db = None
cursor = None
def call_database():
	global db
	global cursor
	db = MySQLdb.connect(host="195.178.232.16", port=3306, user="AC8240", passwd="hejhej123", db="AC8240");
	cursor = db.cursor()
	return cursor

def hang_up_on_database():
    global db
    db = db.close()


def test_sort_by_status():
    cursor=call_database()
    ads=sort_by_status(60, cursor)
    for each in ads:
        assert each[7]=='Obehandlad' or each[7]=='Avslutad' or each[7]=='Bortvald' or each[7]=='Vald'
    hang_up_on_database()


def test_validate_user_true():
    cursor=call_database()
    passing_test=validate_user("stew@dent.se", "abcd", cursor)
    assert passing_test['result']==True
    hang_up_on_database()

def test_validate_user_false():
    cursor=call_database()
    failing_test=validate_user("", "abcd", cursor)
    assert failing_test['result']==False
    hang_up_on_database()

def test_validate_ad_input():
    assert validate_ad_input("")!=True
    assert validate_ad_input(" ")!=True



'''
class TestAddmod(unittest.TestCase):

    def test_validate_ad_input(self):
        res= validate_ad_input("")
        self.assertTrue(res)
    def test_do_ad(self):
        res= do_ad(0)
        self.assertFalse(res['result'])




if __name__=='__main__':
    unittest.main()
'''
