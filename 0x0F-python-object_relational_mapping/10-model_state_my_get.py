#!/usr/bin/python3
"""Module for State class"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

arg = sys.argv
if __name__ == '__main__':
    """Function main"""
    host = 'localhost'
    engine = create_engine(f"mysql://{arg[1]}:{arg[2]}@{host}:3306/{arg[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == arg[4]).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()
