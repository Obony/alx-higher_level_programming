#!/usr/bin/python3
"""
This script a state and its city
"""


def main():
    """
    Create relationship between newly created
    'California' state and newly created 'San Francisco' city
    """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    from relationship_state import Base, State
    from relationship_city import City

    connection = "mysql+mysqldb://{}:{}@localhost/{}".format(str(argv[1]),
                                                             str(argv[2]),
                                                             str(argv[3]))

    engine = create_engine(connection)
    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    california.cities = [City(name="San Francisco")]

    session.add(california)
    session.commit()


if __name__ == '__main__':
    main()
