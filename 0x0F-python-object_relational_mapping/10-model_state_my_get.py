#!/usr/bin/python3
"""
Write a script that prints the State
object with the name passed as argument from the database hbtn_0e_6_usa
Your script should take 4 arguments:
mysql username, mysql password, database name and
state name to search (SQL injection free)
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
You can assume you have one record with the state name to search
Results must display the states.id
If no state has the name you searched for, display Not found
Your code should not be executed when imported
"""
if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sys import argv

    db_uri = (f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")

    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    inst = session.query(State)
    value = inst.filter(State.name.like('{}'.format(argv[4],))).first()

    if value is None:
        print('Not found')
    else:
        print(f"{value.id}")
