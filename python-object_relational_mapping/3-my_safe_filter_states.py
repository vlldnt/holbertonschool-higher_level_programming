#!/usr/bin/python3
'''Safe filter to prevent from SQL injection'''


import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
        )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name=%s ORDER BY id ASC", (sys.argv[4], )
        )
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    db.close()
