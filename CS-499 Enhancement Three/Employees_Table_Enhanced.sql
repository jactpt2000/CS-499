-- ----------------------------------------------------------------------------------
-- Name: Jorge Argueta
-- Course: CS-499
-- Date: 4/6/2024
-- ----------------------------------------------------------------------------------

-- Description: This script sets up the 'Employees_Table' database, containing tables
-- and procedures for managing employee data. It demonstrates advanced MySQL features
-- such as stored procedures and triggers, and connects to the database using Python
-- for data mining and visualization.
-- ----------------------------------------------------------------------------------


-- Check if the database exists and create if it doesn't
CREATE DATABASE IF NOT EXISTS Employees_Table;

-- Select the Employees_Table database for use
USE Employees_Table;

-- Create the Employee table with necessary fields
CREATE TABLE IF NOT EXISTS Employee (
    Employee_ID SMALLINT AUTO_INCREMENT PRIMARY KEY,
    First_Name VARCHAR(40),
    Last_Name VARCHAR(60),
    Department_ID SMALLINT,
    Classification VARCHAR(10),
    Status VARCHAR(10) DEFAULT 'Active',  -- Default status is 'Active'
    Salary DECIMAL(7,2)  -- Salary stored with two decimals
);

-- Create the Branches table to store department details
CREATE TABLE IF NOT EXISTS Branches (
    Department_ID SMALLINT AUTO_INCREMENT PRIMARY KEY,
    Department_Name VARCHAR(50)
);

-- Procedures and Triggers for Automation and Calculations

-- Changes delimiter for complex statements
DELIMITER //

-- Stored procedure to calculate total salary by department
CREATE PROCEDURE Calculate_Total_Salary(IN dept_id SMALLINT)
BEGIN
    -- Sum up salaries where department IDs match
    SELECT SUM(Salary) AS Total_Salary
    FROM Employee
    WHERE Department_ID = dept_id;
END //
DELIMITER ;

-- Reset delimiter to default
DELIMITER //

-- Trigger to update employee status to 'Inactive' if salary drops to 0 or below
DELIMITER //
CREATE TRIGGER Before_Employee_Update
BEFORE UPDATE ON Employee
FOR EACH ROW
BEGIN
    IF NEW.Salary <= 0 THEN
        SET NEW.Status = 'Inactive';  -- Automatically set status to 'Inactive'
    END IF;
END //
DELIMITER ;

-- Python Script for Database Connection and Data Handling

import mysql.connector
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Attempt to establish a database connection
try:
    conn = mysql.connector.connect(
        host="localhost",  -- Database server address
        user="root",       -- Database username
        password="",       -- Password for the database user
        database="Employees_Table"  -- Database name
    )
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
    exit(1)

# Create a cursor object using the connection
cursor = conn.cursor()
