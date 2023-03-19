#!/usr/bin/python3
"""
Write a script that lists all State objects
that contain the letter a from the database hbtn_0e_6_usa
Your script should take 3 arguments:
mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL
server running on localhost at port 3306
Results must be sorted in ascending order by states.id
The results must be displayed as they
are in the example below
Your code should not be executed when imported

"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    """
    List all states that contain the letter a

    """
    db_uri = (f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    instances = session.query(State)
    filtered = instances.filter(State.name.like('%a%')).order_by(State.id)
    for filters in filtered:
        print(f"{filters.id}: {filters.name}")
