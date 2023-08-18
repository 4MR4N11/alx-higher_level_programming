#!/usr/bin/python3
"""Module for State class"""

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """Function main"""
    arg = sys.argv
    host = 'localhost'
    engine = create_engine(f"mysql://{arg[1]}:{arg[2]}@{host}:3306/{arg[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
