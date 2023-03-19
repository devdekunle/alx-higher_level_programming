#!/usr/bin/python3
"""
 a script that prints the first State
 object from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    """
    list the first state
    """
    db_uri = ('mysql+mysqldb://{}:{}@localhost/{}'.format
              (argv[1], argv[2], argv[3]))

    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    result = session.query(State).filter(State.id == 1)
    if result is None:
        print('Nothing')
    for instance in result:
        print(f"{instance.id}: {instance.name}")
