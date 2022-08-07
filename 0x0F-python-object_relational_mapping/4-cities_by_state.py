#!/usr/bin/python3
""" Write a script that lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    con = MySQLdb.connect(host='localhost', port=3306,
                          user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # con is a connection object that represents the database connection and is used to execute SQL statements
    cursor = con.cursor()
    # cursor is a cursor object that is used to traverse the result set of a query
    query = "SELECT * FROM cities INNER JOIN states ON cities.state_id = states.id \
                WHERE states.name LIKE BINARY '{}' ORDER BY cities.id ASC".format(sys.argv[4])
    # query is a string that represents the SQL statement to be executed
    cursor.execute(query)
    # execute() executes a SQL statement and returns the number of rows affected if successful
    rows = cursor.fetchall()
    # fetchall() returns all rows from a query
    for row in rows:
        print(row)
    cursor.close()
    # cursor.close() is used to close the cursor object
    con.close()
    # close() is used to close the connection to the database

