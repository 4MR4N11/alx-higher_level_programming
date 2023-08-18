#!/usr/bin/python3
"""Module for State class"""

import MySQLdb
import sys


if __name__ == '__main__':
    """Function main"""
    args = sys.argv
    db = MySQLdb.connect(
        host='localhost',
        user=args[1],
        password=args[2],
        database=args[3]
    )

    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities\
        INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    db.close()
