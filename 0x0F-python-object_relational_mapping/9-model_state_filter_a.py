#!/usr/bin/python3
"""fetchall module"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")
    session = Session(bind=engine)
    result = session.query(
        State).filter(State.name.like('%a%')).order_by(State.id)
    for row in result:
        print(f"{row.id}: {row.name}")
