#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
that start with a capital N
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    mycursor = mydb.cursor()
    state = sys.argv[4]
    query = "SELECT * FROM states WHERE name = '{}'".format(state)
    mycursor.execute(query)
    rows = mycursor.fetchall()
    for row in rows:
        print(row)

    mycursor.close()
    mydb.close()
