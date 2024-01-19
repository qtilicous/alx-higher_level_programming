#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
            .format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL credentials and state name from command line arguments
    username, password = sys.argv[1], sys.argv[2]
    database, state_name = sys.argv[3], sys.argv[4]

    # Connect to MySQL server
    try:
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Set the collation to case-insensitive for this query
        cursor.execute("SET collation_connection = 'utf8mb4_general_ci'")

        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC LIMIT 1"
        cursor.execute(query, (state_name,))

        # Fetch the first row
        row = cursor.fetchone()

        # Print the result
        if row:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    # Exit the script
    sys.exit(0)
