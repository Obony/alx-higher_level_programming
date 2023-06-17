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

    cursor.execute("SELECT cities.name\
                    FROM cities\
                    JOIN states\
                    ON cities.state_id=states.id\
                    WHERE states.name = %s;", (state_name, ))

    rows = cursor.fetchall()
    cities = []
    for row in rows:
        cities.append(str(row[0]))
    print(', '.join(cities))

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
