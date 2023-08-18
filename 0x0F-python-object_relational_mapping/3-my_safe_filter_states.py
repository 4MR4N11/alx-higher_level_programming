#!/usr/bin/python3
"""Module for State class"""

import MySQLdb
import sys


def escape_spec_char(arg):
    """Function that escapes special characters"""
    if ("'" in arg) or (';' in arg) or ("--" in arg):
        return None
    return arg


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
    query = "SELECT * FROM states WHERE name=%s"
    cursor.execute(query, (escape_spec_char(args[4]),))
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    db.close()
