#!/usr/bin/python3
""" write a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections."""

import MySQLdb
import sys

if __name__ == "__main__":
    con = MySQLdb.connect(host='localhost', port=3306,
                          user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # con is a connection object that represents the database connection and is
    # used to execute SQL statements
    cursor = con.cursor()
    # cursor is a cursor object that is used to traverse the
    # result set of a query
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER \
    BY id ASC".format(sys.argv[4])
    # query is a string that represents the SQL statement to be executed
    cursor.execute(query)
    # execute() executes a SQL statement and returns the number of rows
    # affected if successful
    rows = cursor.fetchall()
    # fetchall() returns all rows from a query
    for row in rows:
        print(row)
    cursor.close()
    # cursor.close() is used to close the cursor object
    con.close()
    # close() is used to close the connection to the database
