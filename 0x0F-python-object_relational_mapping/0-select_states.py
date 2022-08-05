#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

con = MySQLdb.connect(host='localhost', port=3306,
                      user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
# con is a connection object that represents the database connection and is used to execute SQL statements
cursor = con.cursor()
# cursor is a cursor object that is used to traverse the result set of a query
cursor.execute("SELECT * FROM states ORDER BY id ASC")
# execute() executes a SQL statement and returns the number of rows affected if successful
rows = cursor.fetchall()
# fetchall() returns all rows from a query
for row in rows:
    print(row)
con.close()
# close() is used to close the connection to the database
