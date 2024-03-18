#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.
This script takes 3 arguments: mysql username, mysql password, and database name.
It uses the MySQLdb module to connect to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id and displayed as specified.
"""

import MySQLdb
import sys

def connect_to_database(username, password, db_name):
    """
    Connects to the MySQL database with the provided credentials.
    """
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=db_name, charset="utf8")
        return conn
    except MySQLdb.Error as err:
        print(f"Cannot connect to database: {err}")
        sys.exit(1)

def list_states(conn):
    """
    Lists all states from the database in ascending order by their ID.
    """
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
    except MySQLdb.Error as err:
        print(f"SQL Error: {err}")
    finally:
        cur.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    mysql_username, mysql_password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    conn = connect_to_database(mysql_username, mysql_password, database_name)
    list_states(conn)
    conn.close()
