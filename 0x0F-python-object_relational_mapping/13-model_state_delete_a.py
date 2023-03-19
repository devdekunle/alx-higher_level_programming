#!/usr/bin/python3
"""
Write a script that deletes all State objects
with a name containing the letter a from the database hbtn_0e_6_usa
Your script should take 3 arguments:
mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Your code should not be executed when imported

"""
if __name__ == "__main__":
    """
    Access database and delete all states wth letter a
    """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import Base, State

    db_url = (f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    instances = session.query(State).filter(State.name.like('%a%')).all()

    for obj in instances:
        session.delete(obj)

    session.commit()
