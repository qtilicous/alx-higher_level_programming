-- 4. First table
-- Write a script that creates a table called first_table in the current database in your MySQL server.
-- If the table first_table already exists, your script should not fail.
-- You are not allowed to use the SELECT or SHOW statements.

USE `hbtn_0c_0`;

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
