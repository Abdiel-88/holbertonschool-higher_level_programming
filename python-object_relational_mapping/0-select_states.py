#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Unpack command line arguments
    mysql_username, mysql_password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL database
    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                           passwd=mysql_password, db=database_name, charset="utf8")
    # Create a cursor object
    cur = conn.cursor()
    # Execute the SQL query
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch all the rows
    query_rows = cur.fetchall()
    # Iterate and print each row
    for row in query_rows:
        print(row)
    # Close the cursor and connection
    cur.close()
    conn.close()
