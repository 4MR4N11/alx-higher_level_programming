#!/usr/bin/python3
"""Module for State class"""

import MySQLdb
import sys


if __name__ == '__main__':
    """Function main"""
    args = sys.argv
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=args[1],
        password=args[2],
        database=args[3],
    )

    cursor = db.cursor()
    query = "SELECT cities.name FROM cities\
        INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s"
    cursor.execute(query, (args[4],))
    rows = cursor.fetchall()
    keys = []
    for row in rows:
        for key in row:
            keys.append(key)
    print(', '.join(item for item in keys))
    cursor.close()
    db.close()
