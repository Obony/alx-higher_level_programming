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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_city = City(name="San Francisco")
    new_state = State(name="California")
    new_state.cities.append(new_city)
    session.add_all([new_state, new_city])
    session.commit()
    session.close()


if __name__ == '__main__':
    main()
