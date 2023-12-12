# SQL Introduction Project

## Description

This project contains SQL scripts for various tasks related to MySQL.
Each script is designed to be executed on a MySQL server.
The provided script for this task lists all databases on the MySQL server.

## Requirements

- Ubuntu 20.04 LTS
- MySQL 8.0 (version 8.0.25)
- All SQL files should have a comment just before the query
- All SQL keywords should be in uppercase
- The project should have a README.md file
- The README.md file should provide instructions on how to use and execute the SQL script
- The length of your files will be tested using wc

## Installation

1. Install MySQL 8.0 on Ubuntu 20.04 LTS:

    ```bash
    sudo apt update
    sudo apt install mysql-server
    ```

2. Connect to your MySQL server:

    ```bash
    sudo mysql
    ```

3. In the MySQL shell, start MySQL before executing any queries:

    ```bash
    service mysql start
    ```

4. Execute the SQL script to list all databases:

    ```bash
    cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
    ```

    You will be prompted to enter the MySQL root password.

## Contents

- `0-list_databases.sql`: Lists all databases on the MySQL server.

## Author

Azrah Damon <qtilicousbbz@gmail.com>
