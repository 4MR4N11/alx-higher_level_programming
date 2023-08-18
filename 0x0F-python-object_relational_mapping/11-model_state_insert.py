#!/usr/bin/python3
"""Module for State class"""

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

arg = sys.argv
if __name__ == '__main__':
    """Function main"""
    host = 'localhost'
    engine = create_engine(f'mysql://{arg[1]}:{arg[2]}@{host}:3306/{arg[3]}')
    Session = sessionmaker(bind=engine)
    session = Session()

    new = State(name='Louisiana')
    session.add(new)
    session.commit()
    print(new.id)
    session.close()
