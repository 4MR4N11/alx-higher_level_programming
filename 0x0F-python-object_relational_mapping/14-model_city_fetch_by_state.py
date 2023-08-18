#!/usr/bin/python3
"""Module for City class."""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
import sys

arg = sys.argv
if __name__ == '__main__':
    """Function main"""
    host = 'localhost'
    engine = create_engine(f"mysql://{arg[1]}:{arg[2]}@{host}:3306/{arg[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id)
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
