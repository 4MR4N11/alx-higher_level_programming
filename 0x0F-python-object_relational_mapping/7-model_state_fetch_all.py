#!/usr/bin/python3
"""Module for State class"""

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Function main"""
    arg = sys.argv
    host = 'localhost'
    engine = create_engine(f"mysql://{arg[1]}:{arg[2]}@{host}:3306/{arg[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id)

    rows = query.all()
    for row in rows:
        print("{}: {}".format(row.id, row.name))
    session.close()
