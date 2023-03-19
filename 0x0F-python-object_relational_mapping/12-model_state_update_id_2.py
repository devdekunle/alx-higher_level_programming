#!/usr/bin/python3
"""
Write a script that changes the name of a State object
from the database hbtn_0e_6_usa
Your script should take 3 arguments:
mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Change the name of the State where id = 2 to New Mexico
Your code should not be executed when imported
"""
if __name__ == "__main__":
    """
    Access the database and change the name of the state where
    id = 2 to New Mexico
    """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import Base, State

    db_uri = (f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")

    engine = create_engine(db_uri)

    Session = sessionmaker(bind=engine)

    session = Session()

    obj = session.query(State).filter(State.id == 2).first()

    obj.name = 'New Mexico'

    session.commit()
