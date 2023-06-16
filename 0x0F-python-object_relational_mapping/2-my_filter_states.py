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

    query = """SELECT * FROM states WHERE name LIKE '{}' ORDER BY
    id;""".format(argv[4])

    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        if (row[1] == argv[4]):
            print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
