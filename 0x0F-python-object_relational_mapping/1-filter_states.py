#!/usr/bin/python3
""" Write a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    con = MySQLdb.connect(host='localhost', port=3306,
                          user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # con is a connection object that represents the database connection and is
    # used to execute SQL statements
    cursor = con.cursor()
    # cursor is a cursor object that is used to traverse the result
    # set of a query
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    # execute() executes a SQL statement and returns the number of
    # rows affected if successful
    # LIKE is a case-sensitive comparison operator that matches
    # patterns against strings.
    # BINARY is a modifier that forces the comparison to be case-sensitive.
    # N% is a wildcard that matches any string that starts with N and ends
    # with a single character.
    rows = cursor.fetchall()
    # fetchall() returns all rows from a query
    for row in rows:
        print(row)
    con.close()
    # close() is used to close the connection to the database
