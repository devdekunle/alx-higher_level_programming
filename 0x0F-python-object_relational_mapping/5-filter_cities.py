#!/usr/bin/python3
"""
Write a script that takes in the name of a state
as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
Your script should take 4 arguments: mysql username,
mysql password, database name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""
if __name__ == "__main__":
    """
    Access the database and list all cities of a state
    """
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    db_cur = db.cursor()

    db_cur.execute("SELECT c.name \
                   FROM states s \
                   JOIN cities c \
                   ON s.id = c.state_id \
                   WHERE s.name LIKE BINARY %s \
                   ORDER BY c.id ASC", (argv[4],))

    rows = db_cur.fetchall()

    if rows is not None:
        print(", ".join([row[0] for row in rows]))
