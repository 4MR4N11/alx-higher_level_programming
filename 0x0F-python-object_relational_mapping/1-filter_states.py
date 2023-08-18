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
        database=args[3]
    )
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%'\
          ORDER BY states.id"

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    db.close()
