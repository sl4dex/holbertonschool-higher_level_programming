#!/usr/bin/python3
"""Mysqldb filter cities module"""
import MySQLdb
import sys


db = MySQLdb.connect(host="localhost",
                     user=sys.argv[1],
					 passwd=sys.argv[2],
					 db=sys.argv[3])
cur = db.cursor()
cur.execute("""
            SELECT cities.id, cities.name, states.name
			FROM states INNER JOIN cities
			ON states.id=cities.state_id
			ORDER BY cities.id ASC
			""")
for row in cur.fetchall():
    print(row)
