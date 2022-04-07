#!/usr/bin/python3
"""Mysqldb filter states module"""
import MySQLdb
import sys


db = MySQLdb.connect(host="localhost",
                     user=sys.argv[1],
					 passwd=sys.argv[2],
					 db=sys.argv[3])
cur = db.cursor()
cur.execute("""SELECT * FROM states
            WHERE name LIKE '""" + sys.argv[4] + """'
			ORDER BY states.id ASC""")
for row in cur.fetchall():
    print(row)
