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

    states = session.query(State).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))


if __name__ == '__main__':
    main()
