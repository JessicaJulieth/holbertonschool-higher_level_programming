#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities LEFT JOIN states ON\
                cities.state_id = states.id WHERE states.name = %s\
                ORDER BY cities.id", (argv[4], ))

    query_rows = cur.fetchall()
    City = []
    Index = 0
    for row in query_rows:
        City.append(query_rows[Index][0])
        Index += 1
    Cities = ', '.join(City)
    print(Cities)
    cur.close()
    db.close()
