#!/usr/bin/python3
'''
Write a script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa:
Your script should take 3 arguments: mysql username,
mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server
running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Lists all states in the database that starts with lette N
    """
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    db_cur = db.cursor()
    db_cur.execute('SELECT * FROM states WHERE name LIKE "N%"')

    rows = db_cur.fetchall()

    for row in rows:
        print(row)
