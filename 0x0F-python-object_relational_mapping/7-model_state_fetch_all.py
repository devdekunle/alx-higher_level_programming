#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
Your script should take 3 arguments:
mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a
MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
The results must be displayed as they are in the example below
Your code should not be executed when imported

"""

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":

    db_uri = ('mysql+mysqldb://{}:{}@localhost/{}'.format(
              argv[1], argv[2], argv[3]))
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id)

    for instance in result:
        print(f"{instance.id}: {instance.name}")
