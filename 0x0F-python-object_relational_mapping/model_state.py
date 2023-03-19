#!/usr/bin/python3
"""
file that contains the class
definition of a State and an instance Base = declarative_base():

"""
# import utilities from sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv

Base = declarative_base()


# create class to be mapped unto table
class State(Base):
    """
    a class that defines a table of a database in the sql server
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
