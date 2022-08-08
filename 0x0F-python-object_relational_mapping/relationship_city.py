#!/usr/bin/python3
""" Improve the files model_city.py and model_state.py, and save
them as relationship_city.py and relationship_state.py """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import State, Base
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """ This class represents a city in the database """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
