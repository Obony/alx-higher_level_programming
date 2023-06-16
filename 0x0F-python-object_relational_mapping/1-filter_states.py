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

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name REGEXP '^N' ORDER BY id;")
    rows = cursor.fetchall()
    for row in rows:
        if ("N" in row[1]):
            print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
