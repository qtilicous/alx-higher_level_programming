#!/usr/bin/python3
"""
Script that lists all states with a name starting with N
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL credentials from command line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    try:
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        print("Connected to MySQL server.")

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Set the collation to case-insensitive for this query
        cursor.execute("SET collation_connection = 'utf8mb4_general_ci'")

        # Execute the SQL query to get states starting with 'N'
        cursor.execute(
                "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        )

        # Fetch all rows
        rows = cursor.fetchall()

        # Print the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("MySQL connection closed.")

    # Exit the script
    sys.exit(0)
