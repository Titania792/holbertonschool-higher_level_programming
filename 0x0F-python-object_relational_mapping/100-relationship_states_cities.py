#!/usr/bin/python3
""" Write a script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa """

if __name__ == "__main__":
    from sqlalchemy import create_engine, MetaData
    from sys import argv
    from relationship_state import State
    from relationship_city import City, Base
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    nstate = State(name='California')
    ncity = City(name='San Francisco')
    nstate.cities.append(ncity)
    session.add(nstate)
    session.add(ncity)
    session.commit()
    session.close()
