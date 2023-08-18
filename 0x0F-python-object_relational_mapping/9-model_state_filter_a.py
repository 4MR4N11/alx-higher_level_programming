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

    rows = session.query(State)\
        .filter(State.name.like('%a%')).order_by(State.id).all()

    for row in rows:
        print("{}: {}".format(row.id, row.name))
    session.close()
