#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa
Your script should take 3 arguments:
mysql username, mysql password and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server
running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
Results must be displayed as they are in the example below
Your code should not be executed when imported

"""
if __name__ == "__main__":
    """
    Lists all cities by states
    """
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    db_cur = db.cursor()

    db_cur.execute('SELECT c.id, c.name, s.name \
                   FROM states s \
                   JOIN cities c \
                   ON s.id = c.state_id \
                   ORDER BY c.id ASC;')

    rows = db_cur.fetchall()
    for row in rows:
        print(row)
