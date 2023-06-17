#!/usr/bin/python3
"""
This module lists all states from 'hbtn_0e_6_usa' database
"""


def main():
    """
    List all 'States' table objects in 'hbtn_0e_usa' database
    """
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from sys import argv

    from model_state import Base, State

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
