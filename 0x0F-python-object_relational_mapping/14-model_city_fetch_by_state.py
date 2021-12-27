#!/usr/bin/python3
""" script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newt = session.query(State, City).filter(City.state_id == State.id).order_by(City.id).all()
    for cities, state in newt:
        print('{}: ({}) {}'.format(state.name, cities.id, cities.name))
    session.close()
