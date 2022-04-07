#!/usr/bin/python3
"""Mysqldb cities by state module"""
import MySQLdb
import sys


db = MySQLdb.connect(host="localhost",
                     user=sys.argv[1],
					 passwd=sys.argv[2],
					 db=sys.argv[3])
cur = db.cursor()
cur.execute("""
            SELECT cities.name
			FROM states INNER JOIN cities
			ON states.id=cities.state_id
			WHERE states.name=%s
			ORDER BY cities.id ASC
			""", (sys.argv[4],))
result = cur.fetchall();
if len(result) == 0:
    print()
for i in range(len(result)):
    if i == len(result) - 1:
	    print(result[i][0])
    else:
        print(result[i][0], end=", ")
