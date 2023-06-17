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

    cursor.execute("SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')\
                    FROM cities\
                    JOIN states\
                    ON cities.state_id=states.id\
                    WHERE cities.state_id=states.id\
                    AND states.name=%s\
                    ORDER BY cities.id ASC;", (state_name, ))

    rows = cursor.fetchall()
    for row in rows:
        if row[0] is not one:
            print(row[0])
        else:
            print()

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
