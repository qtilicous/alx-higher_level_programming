#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

        try:
            connection = MySQLdb.connect(
                    host="localhost",
                    port=3306,
                    user=username,
                    passwd=password,
                    db=database
                    )
        except MySQLdb.Error as e:
            print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
            sys.exit(1)

            cursor = connection.cursor()

            query = "SELECT * FROM states ORDER BY id ASC"
            cursor.execute(query)

            rows = cursor.fetchall()

            for row in rows:
                print(row)

                cursor.close()
                connection.close()
