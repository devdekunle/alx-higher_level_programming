#!/usr/bin/python3
"""
Write a script that adds the State
object “Louisiana” to the database hbtn_0e_6_usa
Your script should take 3 arguments:
mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a
MySQL server running on localhost at port 3306
Print the new states.id after creation
Your code should not be executed when imported
"""
if __name__ == "__main__":
    """
    Access the database and add a new state
    the print its id
    """
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    db_uri = (f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    engine = create_engine(db_uri)

    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)

    session.commit()

    print(f"{new_state.id}")
    session.close()
