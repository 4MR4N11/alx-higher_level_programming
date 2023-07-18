--This script displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
SELECT COUNT(*) AS number_of_records
FROM first_table
WHERE id = 89;