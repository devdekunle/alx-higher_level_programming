#!/usr/bin/python3
"""
Write a script that prints the first
State object from the database hbtn_0e_6_usa
Your script should take 3 arguments:
mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server
running on localhost at port 3306
The state you display must be the first in states.id
You are not allowed to fetch all states
from the database before displaying the result
The results must be displayed
as they are in the example below
If the table states is empty,
print Nothing followed by a new line
Your code should not be executed when imported
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    """
    list the first state from the database hbtn_0e_6_usa
    """
    db_uri = ('mysql+mysqldb://{}:{}@localhost/{}'.format
              (argv[1], argv[2], argv[3]))

    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    instance = session.query(State).order_by(State.id).first()
    if instance is None:
        print('Nothing')
    else:
        print(f"{instance.id}: {instance.name}")
