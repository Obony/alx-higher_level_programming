#!/usr/bin/python3
"""
Listing all states from the database hbtn_0e_0_usa
"""


def main():
    """
    List 'states' table of 'hbtn_0e_0_usa' database in ascending
    order by id's
    """
    import MySQLdb
    from sys import argv

    usr = str(argv[1])
    pasw = str(argv[2])
    db_name = str(argv[3])
    state_name = str(argv[4])

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=usr, passwd=pasw, db=db_name)
    cursor = db.cursor()

    query = cur.execute("SELECT * FROM states WHERE name LIKE ( %s );",
                (state_name, ))
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
