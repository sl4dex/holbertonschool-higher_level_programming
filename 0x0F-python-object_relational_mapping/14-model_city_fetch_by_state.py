#!/usr/bin/python3
"""update state module"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")
    session = Session(bind=engine)
    rows = session.query(State).join(City)
    for stat in rows:
        for cit in stat.cities:
            print(f"{stat.name}: ({cit.id}) {cit.name}")