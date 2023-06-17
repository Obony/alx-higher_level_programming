#!/usr/bin/python3
"""
This module lists all cities from a database
"""


def main():
    """
    List all 'Cities' table objects in a given database
    """
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from sys import argv

    from model_state import Base, State
    from model_city import City

    connection = "mysql+mysqldb://{}:{}@localhost/{}".format(str(argv[1]),
                                                             str(argv[2]),
                                                             str(argv[3]))
    engine = create_engine(connection)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities_by_states = session.query(City, State).\
        filter(City.state_id == State.id).all()
    for city, state in cities_by_states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))


if __name__ == '__main__':
    main()
