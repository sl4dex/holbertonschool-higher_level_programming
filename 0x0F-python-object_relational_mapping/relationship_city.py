#!/usr/bin/python3
"""SQLalchemy city module"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """City class"""
    __tablename__ = 'cities'
    # pk=True sets autoincrement=True and nullable=False
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State")
