#!/usr/bin/python3
"""SQLalchemy state module"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import City

Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'
    # pk=True sets autoincrement=True and nullable=False
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete")
