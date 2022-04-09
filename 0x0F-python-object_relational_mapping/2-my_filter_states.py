#!/usr/bin/python3
"""Mysqldb filter states module"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    query = """SELECT * FROM states
               WHERE name LIKE '{}'
               ORDER BY states.id ASC""".format(sys.argv[4])
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
