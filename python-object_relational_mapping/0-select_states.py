#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

def list_states(mysql_username, mysql_password, database_name):
    """
    Lists all states from the database.
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                           passwd=mysql_password, db=database_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        mysql_username, mysql_password, database_name = sys.argv[1:4]
        list_states(mysql_username, mysql_password, database_name)
