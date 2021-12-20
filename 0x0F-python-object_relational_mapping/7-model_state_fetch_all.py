#!/usr/bin/python3
""" script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'\
                    .format(sys.argv[1], sys.argv[2], sys.argv[3]),\
                    pool_pre_ping=True)
    Base.metadata.create_all(engine)

Session = sessionmaker()
session = Session(engine)
for states in session.query(State).order_by(State.id).all():
    print(states.id, ':', states.name)
