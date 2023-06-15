#!/usr/bin/python3
import sys
import MySQLdb


def list_states(username, password, db_name):
    '''
        Listing all states in hbtn_0e_0_usa database
        in ascending order by id's.
    '''
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

if __name__ == "__main__":
    credentials = sys.argv
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    list_states(username, passwd, db_name)
